from django.apps import AppConfig

from advanced_options.enums import VerboseNamePluralEnum


class AdvancedOptionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'advanced_options'
    verbose_name = VerboseNamePluralEnum.ADVANCED_OPTION.value
