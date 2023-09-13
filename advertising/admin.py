from django.contrib import admin

from advertising.models import Advertising


@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'created_at',
        'updated_at'
    )

    readonly_fields = (
        'created_at',
        'updated_at'
    )
