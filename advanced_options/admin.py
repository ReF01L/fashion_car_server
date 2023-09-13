from django.contrib import admin

from advanced_options.enums import VerboseNamePluralEnum
from advanced_options.models import AdvancedOption
from orders.models import Order, ServiceOrder, Sale
from products.models import Product


class AdvancedOptionOrderInline(admin.TabularInline):
    model = Order.advanced_options.through
    extra = 1
    verbose_name = VerboseNamePluralEnum.ORDER_OPTION.value


class AdvancedOptionServiceOrderInline(admin.TabularInline):
    model = ServiceOrder.advanced_options.through
    extra = 1
    verbose_name = VerboseNamePluralEnum.ORDER_SERVICE_OPTION.value


class AdvancedOptionProductInline(admin.TabularInline):
    model = Product.advanced_options.through
    extra = 1
    verbose_name = VerboseNamePluralEnum.PRODUCT_OPTION.value


class AdvancedOptionSaleInline(admin.TabularInline):
    model = Sale.advanced_options.through
    extra = 1
    verbose_name = VerboseNamePluralEnum.SALE_OPTION.value


@admin.register(AdvancedOption)
class AdvancedOptionAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')
