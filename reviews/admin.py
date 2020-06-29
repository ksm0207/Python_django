from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """ Review Admin Definition(리뷰 관리자 정의)"""

    list_display = ('__str__', "rating_average")
