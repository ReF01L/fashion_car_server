from django.apps import AppConfig

from orders.enums import VerboseNamePluralEnum


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'

    verbose_name = VerboseNamePluralEnum.ORDER.value
