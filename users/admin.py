from django.contrib import admin
from django.contrib.auth.models import Group

from .enums import VerboseNameEnum
from .forms import UserForm
from .models import Client, Manager, Provider, Master, User

admin.site.unregister(Group)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    form = UserForm
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'second_name',
                'patronymic',
                'phone',
            ),
        }),
    )
    list_select_related = ('user',)
    list_display = (
        'name',
        'second_name',
        'patronymic',
        'phone',
    )

    @admin.display(boolean=True, description=VerboseNameEnum.IS_ACTIVE.value)
    def is_active(self, obj: Client):
        return obj.user.is_active

    @admin.display(empty_value='???', description=VerboseNameEnum.USER_NAME.value)
    def name(self, obj: Client):
        return obj.user.name

    @admin.display(empty_value='Не указано', description=VerboseNameEnum.SECOND_NAME.value)
    def second_name(self, obj: Client):
        return obj.user.second_name

    @admin.display(empty_value='Не указано', description=VerboseNameEnum.PATRONYMIC.value)
    def patronymic(self, obj: Client):
        return obj.user.patronymic

    @admin.display(empty_value='Не указано', description=VerboseNameEnum.PHONE.value)
    def phone(self, obj: Client):
        return obj.user.phone

    def get_form(self, request, obj, change, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)

        if obj is not None:
            form.declared_fields['name'].initial = obj.user.name
            form.declared_fields['second_name'].initial = obj.user.second_name
            form.declared_fields['patronymic'].initial = obj.user.patronymic
            form.declared_fields['phone'].initial = obj.user.phone

        return form

    def save_model(self, request, obj, form, change) -> None:
        user_data = {
            'name': form.cleaned_data['name'],
            'second_name': form.cleaned_data['second_name'],
            'patronymic': form.cleaned_data['patronymic'],
        }
        if change:
            user = obj.user
            for key, value in user_data.items():
                setattr(user, key, value)
            user.save()
            obj.save()

        else:
            user = User.objects.create_user(
                phone=form.cleaned_data['phone'],
                password=User.objects.make_random_password(10),
                **user_data
            )

            obj.user = user
            obj.save()


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    form = UserForm
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'second_name',
                'patronymic',
                'phone',
                'salary',
                'additional_percent'
            ),
        }),
    )
    list_select_related = ('user',)
    list_display = (
        'name',
        'second_name',
        'patronymic',
        'phone',
        'salary',
        'additional_percent'
    )

    @admin.display(boolean=True, description=VerboseNameEnum.IS_ACTIVE.value)
    def is_active(self, obj: Manager):
        return obj.user.is_active

    @admin.display(empty_value='???', description=VerboseNameEnum.USER_NAME.value)
    def name(self, obj: Manager):
        return obj.user.name

    @admin.display(empty_value='Не указано', description=VerboseNameEnum.SECOND_NAME.value)
    def second_name(self, obj: Manager):
        return obj.user.second_name

    @admin.display(empty_value='Не указано', description=VerboseNameEnum.PATRONYMIC.value)
    def patronymic(self, obj: Manager):
        return obj.user.patronymic

    @admin.display(empty_value='Не указано', description=VerboseNameEnum.PHONE.value)
    def phone(self, obj: Manager):
        return obj.user.phone

    def get_form(self, request, obj, change, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)

        if obj is not None:
            form.declared_fields['name'].initial = obj.user.name
            form.declared_fields['second_name'].initial = obj.user.second_name
            form.declared_fields['patronymic'].initial = obj.user.patronymic
            form.declared_fields['phone'].initial = obj.user.phone

        return form

    def save_model(self, request, obj, form, change) -> None:
        user_data = {
            'name': form.cleaned_data['name'],
            'second_name': form.cleaned_data['second_name'],
            'patronymic': form.cleaned_data['patronymic'],
            'is_staff': True
        }
        if change:
            user = obj.user
            for key, value in user_data.items():
                setattr(user, key, value)
            user.save()
            obj.save()

        else:
            user = User.objects.create_user(
                phone=form.cleaned_data['phone'],
                password=User.objects.make_random_password(10),
                **user_data
            )
            obj.user = user
            obj.salary = form.cleaned_data['salary']
            obj.additional_percent = form.cleaned_data['additional_percent']

            obj.save()


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    form = UserForm
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'second_name',
                'patronymic',
                'phone',
                'salary',
                'additional_percent'
            ),
        }),
    )
    list_select_related = ('user',)
    list_display = (
        'name',
        'second_name',
        'patronymic',
        'phone',
        'salary',
        'additional_percent'
    )

    @admin.display(boolean=True, description=VerboseNameEnum.IS_ACTIVE.value)
    def is_active(self, obj: Master):
        return obj.user.is_active

    @admin.display(empty_value='???', description=VerboseNameEnum.USER_NAME.value)
    def name(self, obj: Master):
        return obj.user.name

    @admin.display(empty_value='Не указано', description=VerboseNameEnum.SECOND_NAME.value)
    def second_name(self, obj: Master):
        return obj.user.second_name

    @admin.display(empty_value='Не указано', description=VerboseNameEnum.PATRONYMIC.value)
    def patronymic(self, obj: Master):
        return obj.user.patronymic

    @admin.display(empty_value='Не указано', description=VerboseNameEnum.PHONE.value)
    def phone(self, obj: Master):
        return obj.user.phone

    def get_form(self, request, obj, change, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)

        if obj is not None:
            form.declared_fields['name'].initial = obj.user.name
            form.declared_fields['second_name'].initial = obj.user.second_name
            form.declared_fields['patronymic'].initial = obj.user.patronymic
            form.declared_fields['phone'].initial = obj.user.phone

        return form

    def save_model(self, request, obj, form, change) -> None:
        user_data = {
            'name': form.cleaned_data['name'],
            'second_name': form.cleaned_data['second_name'],
            'patronymic': form.cleaned_data['patronymic']
        }
        if change:
            user = obj.user
            for key, value in user_data.items():
                setattr(user, key, value)
            user.save()
            obj.save()

        else:
            user = User.objects.create_user(
                phone=form.cleaned_data['phone'],
                password=User.objects.make_random_password(10),
                **user_data
            )
            obj.user = user
            obj.salary = form.cleaned_data['salary']
            obj.additional_percent = form.cleaned_data['additional_percent']

            obj.save()


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'owner_name'
    )
