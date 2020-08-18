import datetime
from django.http import Http404
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from rooms import models as room_models
from django.views.generic import View, ListView
from reviews import forms as review_forms
from . import models
from django.contrib.auth.decorators import login_required


class CreateError(Exception):
    pass


@login_required
def create(request, room, year, month, day):

    try:
        date_obj = datetime.datetime(year, month, day)
        room = room_models.Room.objects.get(pk=room)
        models.BookedDay.objects.get(day=date_obj, reservation__room=room)
        raise CreateError()
    except (room_models.Room.DoesNotExist, CreateError):
        messages.error(request, "선택하신 방은 예약 할수 없는 방 입니다.")
        return redirect(reverse("core:home"))

    except models.BookedDay.DoesNotExist:
        reservation = models.Reservation.objects.create(
            guest=request.user,
            room=room,
            check_in=date_obj,
            check_out=date_obj + datetime.timedelta(days=1),
        )
        return redirect(reverse("reservations:detail", kwargs={"pk": reservation.pk}))


class ReservationDetailView(View):
    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        reservation = models.Reservation.objects.get_or_none(pk=pk)
        if not reservation or (
            reservation.guest != self.request.user
            and reservation.room.host != self.request.user
        ):
            return redirect(reverse("core:home"))
        form = review_forms.CreateReviewForm()
        return render(
            self.request,
            "reservations/detail.html",
            {"reservation": reservation, "form": form},
        )


def edit_reservation(request, pk, verb):
    reservation = models.Reservation.objects.get_or_none(pk=pk)
    if not reservation or (
        reservation.guest != request.user and reservation.room.host != request.user
    ):
        raise Http404()
    if verb == "confirm":
        reservation.status = models.Reservation.STATUS_CONFIRMED
        messages.success(request, "예약을 확인하였습니다.")
      
    elif verb == "cancel":
        reservation.status = models.Reservation.STATUS_CANCELED
        models.BookedDay.objects.filter(reservation=reservation)
        models.Reservation.objects.filter(pk=pk)
        messages.success(request, "예약을 취소하였습니다.")
    elif verb == "canceled":
        models.Reservation.objects.filter(pk=pk).delete()
        return redirect(reverse("reservations:see-reservation"))

    reservation.save()
    return redirect(reverse("reservations:detail", kwargs={"pk": reservation.pk}))
    # return redirect(reverse("reservations:detail", kwargs={"pk": reservation.pk}))


class SeeReservation(ListView):
    template_name = "reservations/reservation_list.html"
    model = models.Reservation
    paginate_by = 12
    paginate_orphans = 1
    ordering = "created"
    context_object_name = "reservations"

    def get_queryset(self):
        # 중단점 라인번호 클릭
        # A
        reservation = super().get_queryset()
     
        return reservation


class HostReservationList(ListView):
    template_name = "reservations/reservation_host.html"
    model = models.Reservation
    context_object_name = "reservations"

    def get_queryset(self):

        reservation_list = super().get_queryset()
        return reservation_list

