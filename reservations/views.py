import datetime
from django.http import Http404
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from rooms import models as room_models
from django.views.generic import View, ListView
from reviews import forms as review_forms
from . import models


class CreateError(Exception):
    pass


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
            raise Http404()
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
    elif verb == "cancel":
        reservation.status = models.Reservation.STATUS_CANCELED
        models.BookedDay.objects.filter(reservation=reservation).delete()
    reservation.save()
    messages.success(request, "선택하신 예약취소 요청이 완료 되었습니다.")
    return redirect(reverse("reservations:detail", kwargs={"pk": reservation.pk}))


class SeeReservation(ListView):
    template_name = "reservations/reservation_list.html"
    model = models.Reservation
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "reservations"

    def get_queryset(self):
        photos = super().get_queryset()
        print(photos)
        return photos

    # the_reservation = reservation_models.Reservation.objects.get_or_none(guest=user)
    # print(the_reservation)


# class ReservationListView(View):
#     pass
# def get(self, *args, **kwargs):
#     pk = kwargs.get("pk")
#     reservation = models.Reservation.objects.get_or_none(pk=pk)
#     print(reservation)
#     if not reservation:
#         raise Http404()
#     return render(
#         self.request,
#         "reservations/reservation_list.html",
#         {"reservation": reservation},
#     )
# """ HomeView Definition (홈뷰 유형 정의)"""


# template_name = "reservations/reservation_list.html"

