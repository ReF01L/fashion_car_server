from django.forms import ModelForm, CharField, ValidationError

from users.enums import VerboseNameEnum
from users.models import User
from users.validators import phone_validator


class UserForm(ModelForm):
    name = CharField(max_length=64, label=VerboseNameEnum.USER_NAME.value)
    second_name = CharField(max_length=64, label=VerboseNameEnum.SECOND_NAME.value)
    patronymic = CharField(max_length=64, label=VerboseNameEnum.PATRONYMIC.value)
    phone = CharField(
        validators=(phone_validator,),
        max_length=10,
        label=VerboseNameEnum.PHONE.value
    )

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if User.objects.filter(phone=phone).exists():
            raise ValidationError('Пользователь с таким телефоном уже существует!')

        return phone
