from django.urls import path
from . import views

app_name = "conversations"

urlpatterns = [
    path("go/<int:host_pk>/<int:guest_pk>", views.go_conversation, name="go")
]
