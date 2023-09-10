from django.db import models

from services.enums import VerboseNameEnum, VerboseNamePluralEnum


class Service(models.Model):
    name = models.CharField(max_length=64, verbose_name=VerboseNameEnum.NAME.value)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = VerboseNameEnum.SERVICE.value
        verbose_name_plural = VerboseNamePluralEnum.SERVICE.value
