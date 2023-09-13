from django.apps import AppConfig

from advertising.enums import VerboseNamePluralEnum


class AdvertisingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'advertising'
    verbose_name = VerboseNamePluralEnum.ADVERTISING.value
