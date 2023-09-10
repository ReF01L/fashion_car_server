from django.db import models

from services.enums import VerboseNameEnum


class Service(models.Model):
    name = models.CharField(max_length=64, verbose_name=VerboseNameEnum.NAME.value)
