from django.shortcuts import render
from django.db.models import Q
from users import models as user_models
from . import models


def go_conversation(request, host_pk, guest_pk):
    user_one = user_models.User.objects.get_or_none(pk=host_pk)
    user_two = user_models.User.objects.get_or_none(pk=guest_pk)
    if user_one is not None and user_two is not None:
        conversation = models.Conversation.objects.get(
            Q(participants=user_one) & Q(participants=user_two)
        )
        print(conversation)
