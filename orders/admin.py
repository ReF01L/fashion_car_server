from django.contrib import admin
from itertools import zip_longest

from products.models import Product
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

    def save_model(self, request, obj: Order, form, change):
        super().save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        order = formsets[0].instance
        return super().save_related(request, form, formsets, change)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'provider'
    )


@admin.register(ServiceOrder)
class ServiceOrderAdmin(admin.ModelAdmin):
    list_display = (
        'auto',
        'sale_price',
        'expenses',
        'service'
    )
