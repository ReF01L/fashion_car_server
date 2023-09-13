from django.apps import AppConfig

from automobile.enums import VerboseNamePluralEnum


class AutomobileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'automobile'
    verbose_name = VerboseNamePluralEnum.AUTO.value
