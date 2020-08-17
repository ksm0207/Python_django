from django.urls import path
from . import views

app_name = "conversations"

urlpatterns = [
    path("go/<int:host_pk>/<int:guest_pk>/", views.go_conversation, name="go"),
    path("<int:pk>/", views.ConversationDetailView.as_view(), name="detail"),
    path("message/", views.SeeMessageView.as_view(), name="message")
]

