from django.contrib import admin
from itertools import zip_longest

from products.models import Product
from .enums import VerboseNameEnum
from .filters import OrderDateFilter, OrderStatusFilter
from .forms import OrderForm
from .models import Order, OrderItem, ServiceOrder


class OrderItemsInline(admin.StackedInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # form = OrderForm
    # fieldsets = (
    #     (None, {
    #         'fields': (
    #             'client',
    #             'manager',
    #             'state',
    #             'order_items'
    #         ),
    #     }),
    # )

    list_display = (
        'created_at',
        'updated_at',
        'client',
        'manager',
        'state'
    )

    list_filter = (
        (OrderDateFilter, OrderStatusFilter)
    )

    inlines = (OrderItemsInline,)

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

    @admin.display(description=VerboseNameEnum.RESULT.value)
    def result(self, obj: ServiceOrder):
        return f'{obj.sale_price - obj.expenses}'
