from django.contrib.auth.base_user import AbstractBaseUser

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models, transaction

from users.managers import UserManager
from users.validators import phone_validator
from users.enums import VerboseNameEnum, VerboseNamePluralEnum


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=64, verbose_name=VerboseNameEnum.USER_NAME.value)
    second_name = models.CharField(
        max_length=64,
        verbose_name=VerboseNameEnum.SECOND_NAME.value,
        null=True,
        default=None
    )
    patronymic = models.CharField(
        max_length=64,
        verbose_name=VerboseNameEnum.PATRONYMIC.value,
        null=True,
        default=None
    )

    phone = models.CharField(
        validators=(phone_validator,),
        max_length=16,
        verbose_name=VerboseNameEnum.PHONE.value,
        unique=True
    )

    is_active = models.BooleanField(default=True, verbose_name=VerboseNameEnum.IS_ACTIVE.value)
    is_staff = models.BooleanField(default=False, verbose_name=VerboseNameEnum.IS_STAFF.value)
    is_superuser = models.BooleanField(default=False, verbose_name=VerboseNameEnum.IS_SUPERUSER.value)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=VerboseNameEnum.CREATED_AT.value)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=VerboseNameEnum.UPDATED_AT.value)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.name}'

    class Meta:
        verbose_name = VerboseNameEnum.CLIENT.value
        verbose_name_plural = VerboseNamePluralEnum.CLIENT.value


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=VerboseNameEnum.SALARY.value)
    additional_percent = models.PositiveIntegerField(verbose_name=VerboseNameEnum.ADDITIONAL_PERCENT.value)

    def __str__(self):
        return f'{self.user.second_name} {self.user.name}'

    class Meta:
        verbose_name = VerboseNameEnum.MANAGER.value
        verbose_name_plural = VerboseNamePluralEnum.MANAGER.value


class Master(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=VerboseNameEnum.SALARY.value)
    additional_percent = models.PositiveIntegerField(verbose_name=VerboseNameEnum.ADDITIONAL_PERCENT.value)

    def __str__(self):
        return f'{self.user.second_name} {self.user.name}'

    class Meta:
        verbose_name = VerboseNameEnum.MASTER.value
        verbose_name_plural = VerboseNamePluralEnum.MASTER.value


class Provider(models.Model):
    name = models.CharField(max_length=64, verbose_name=VerboseNameEnum.PROVIDER.value)
    owner_name = models.CharField(max_length=64, verbose_name=VerboseNameEnum.USER_NAME.value)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = VerboseNameEnum.PROVIDER.value
        verbose_name_plural = VerboseNamePluralEnum.PROVIDER.value
