from django.apps import AppConfig

from services.enums import VerboseNameEnum


class ServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services'

    verbose_name = VerboseNameEnum.SERVICE.value
