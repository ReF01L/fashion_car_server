from django.db import models

from advertising.enums import VerboseNameEnum, VerboseNamePluralEnum


class Advertising(models.Model):
    name = models.CharField(max_length=128, verbose_name=VerboseNameEnum.NAME.value)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=VerboseNameEnum.EXPENSES.value)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=VerboseNameEnum.CREATED_AT.value)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=VerboseNameEnum.UPDATED_AT.value)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = VerboseNameEnum.ADVERTISING.value
        verbose_name_plural = VerboseNamePluralEnum.ADVERTISING.value