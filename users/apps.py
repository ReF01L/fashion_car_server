from django.apps import AppConfig

from users.enums import VerboseNamePluralEnum


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    verbose_name = VerboseNamePluralEnum.USER.value
