from dateutil.relativedelta import relativedelta
from django.contrib import admin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from products.enums import UnusedProductsEnum, VerboseNameEnum
from products.models import Product


class ProductUnusedFilter(admin.SimpleListFilter):
    title = _(VerboseNameEnum.UNUSED_PRODUCTS.value)
    parameter_name = 'daterange'

    def lookups(self, request, model_admin):
        return (
            (x.name, x.value) for x in UnusedProductsEnum
        )

    def queryset(self, request, queryset):
        today = timezone.now().date()
        queryset = Product.objects.all()

        if self.value() == UnusedProductsEnum.QUARTER_BY_3_MONTHS.name:
            return queryset.exclude(
                orderitem__order__created_at__lte=today,
                orderitem__order__created_at__gte=today - relativedelta(months=3)
            )

        elif self.value() == UnusedProductsEnum.QUARTER_BY_6_MONTHS.name:
            return queryset.exclude(
                orderitem__order__created_at__lte=today,
                orderitem__order__created_at__gte=today - relativedelta(months=6)
            )

        elif self.value() == UnusedProductsEnum.QUARTER_BY_12_MONTHS.name:
            return queryset.exclude(
                orderitem__order__created_at__lte=today,
                orderitem__order__created_at__gte=today - relativedelta(months=12)
            )

        return queryset
