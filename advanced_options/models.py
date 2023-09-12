from django.db import models

from advanced_options.enums import VerboseNameEnum, VerboseNamePluralEnum


class AdvancedOption(models.Model):
    key = models.CharField(max_length=64, verbose_name=VerboseNameEnum.KEY.value)
    value = models.TextField(verbose_name=VerboseNameEnum.VALUE.value)

    def __str__(self):
        return f'{self.key}: {self.value}'

    class Meta:
        verbose_name = VerboseNameEnum.ADVANCED_OPTION.value
        verbose_name_plural = VerboseNamePluralEnum.ADVANCED_OPTION.value
