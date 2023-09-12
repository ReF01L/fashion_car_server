from django.contrib import admin
from django.db.models import Sum

from advanced_options.admin import AdvancedOptionOrderInline, AdvancedOptionServiceOrderInline
from .enums import VerboseNameEnum
from .filters import OrderDateFilter, OrderStatusFilter
from .models import Order, OrderItem, ServiceOrder


class OrderItemsInline(admin.StackedInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'updated_at',
        'client',
        'manager',
        'state',
        'additional_expenses',
        'sale_price',
        'expenses',
        'result'
    )

    exclude = ('advanced_options',)

    list_filter = (
        (OrderDateFilter, OrderStatusFilter)
    )

    inlines = (AdvancedOptionOrderInline, OrderItemsInline)

    @admin.display(empty_value='Нет цены', description=VerboseNameEnum.SALE_PRICE.value)
    def sale_price(self, order: Order):
        return order.orderitem_set.aggregate(
            Sum('product__price__sale_price')
        ).get('product__price__sale_price__sum')

    @admin.display(empty_value='Нет цены', description=VerboseNameEnum.EXPENSES.value)
    def expenses(self, order: Order):
        return order.orderitem_set.aggregate(
            Sum('product__price__purchase_price')
        ).get('product__price__purchase_price__sum')

    @admin.display(empty_value='Нет цены', description=VerboseNameEnum.RESULT.value)
    def result(self, order: Order):
        sale_price = order.orderitem_set.aggregate(
            Sum('product__price__sale_price')
        ).get('product__price__sale_price__sum')
        purchase_price = order.orderitem_set.aggregate(
            Sum('product__price__purchase_price')
        ).get('product__price__purchase_price__sum')

        if sale_price is None or purchase_price is None:
            return None

        return sale_price - purchase_price - order.additional_expenses

    def save_related(self, request, form, formsets, change):
        order = formsets[0].instance

        for product in order.orderitem_set.all():
            product.product.increased()

        super().save_related(request, form, formsets, change)

        for product in order.orderitem_set.all():
            product.product.sell()


@admin.register(ServiceOrder)
class ServiceOrderAdmin(admin.ModelAdmin):
    list_display = (
        'auto',
        'service',
        'client',
        'manager',
        'state',
        'sale_price',
        'expenses',
        'result',
        'created_at',
        'updated_at',
    )

    exclude = ('advanced_options',)

    list_filter = (
        (OrderDateFilter, OrderStatusFilter)
    )

    inlines = (AdvancedOptionServiceOrderInline,)

    @admin.display(description=VerboseNameEnum.RESULT.value)
    def result(self, obj: ServiceOrder):
        return f'{obj.sale_price - obj.expenses}'
