from . import models
from django.shortcuts import render
from django_countries import countries
from django.views.generic import ListView, DetailView


class HomeView(ListView):
    """ HomeView Definition (홈뷰 유형 정의)"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """RoomDetail Definition """

    model = models.Room


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    room_types = models.RoomType.objects.all()

    form = {
        "city": city,
        "s_room_type": room_type,
        "s_country": country,
    }

    choices = {
        "countries": countries,
        "room_types": room_types,
    }
    return render(request, "rooms/search.html", {**form, **choices})
