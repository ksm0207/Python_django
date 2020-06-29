from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    """ List Admin Definition 리스트 유형 정의 """

    list_display = ("name", "user", "count_rooms")

    search_fields = ("^name",)

    filter_horizontal = ("rooms",)
