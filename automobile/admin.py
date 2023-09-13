from django.contrib import admin

from automobile.enums import RudderTypeEnum, DriveEnum
from automobile.models import Auto


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'year',
        'rudder',
        'drive'
    )
