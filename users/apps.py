from django.apps import AppConfig

from users.enums import VerboseNameEnum


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    verbose_name = VerboseNameEnum.USER.value
