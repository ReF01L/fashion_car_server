from django.db import models

from automobile.enums import RudderTypeEnum, VerboseNameEnum, DriveEnum


class Auto(models.Model):
    name = models.CharField(max_length=128, verbose_name=VerboseNameEnum.NAME.value)
    year = models.PositiveIntegerField(verbose_name=VerboseNameEnum.YEAR.value)
    rudder = models.CharField(
        max_length=8,
        choices=(
            (x.name, x.value) for x in RudderTypeEnum
        ),
        verbose_name=VerboseNameEnum.RUDDER.value
    )
    drive = models.CharField(
        max_length=8,
        choices=(
            (x.name, x.value) for x in DriveEnum
        ),
        verbose_name=VerboseNameEnum.DRIVE.value
    )

    def __str__(self):
        return f'{self.name} {self.year} {self.rudder} {self.drive}'
