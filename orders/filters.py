from dateutil.relativedelta import relativedelta

from django.contrib import admin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .enums import StatusEnum


class OrderDateFilter(admin.SimpleListFilter):
    title = _('Заказы за')
    parameter_name = 'created_at'

    def lookups(self, request, model_admin):
        return (
            (_('1 Months'), _('Последние 1')),
            (_('3 Months'), _('Последние 3')),
            (_('6 Months'), _('Последние 6')),
            (_('12 Months'), _('Последние 12')),
        )

    def queryset(self, request, queryset):
        today = timezone.now().date()
        if self.value() == '1 Months':
            return queryset.filter(
                created_at__lte=today,
                created_at__gte=today - relativedelta(months=1)
            )
        elif self.value() == '3 Months':
            return queryset.filter(
                created_at__lte=today,
                created_at__gte=today - relativedelta(months=3)
            )
        elif self.value() == '6 Months':
            return queryset.filter(
                created_at__lte=today,
                created_at__gte=today - relativedelta(months=6)
            )
        elif self.value() == '12 Months':
            return queryset.filter(
                created_at__lte=today,
                created_at__gte=today - relativedelta(months=12)
            )
        return queryset


class OrderStatusFilter(admin.SimpleListFilter):
    title = _('Фильтр по статусам')
    parameter_name = 'state'

    def lookups(self, request, model_admin):
        return (
            (x.name, x.value) for x in StatusEnum
        )

    def queryset(self, request, queryset):
        status = self.value()
        if status is None:
            return queryset.filter(
                state__in=(
                    StatusEnum.WAIT.name,
                    StatusEnum.PROGRESS.name,
                    StatusEnum.READY.name
                )
            )

        return queryset.filter(state=StatusEnum[status].name)
