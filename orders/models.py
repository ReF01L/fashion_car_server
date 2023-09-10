from django.db import models

from orders.enums import StatusEnum, VerboseNameEnum, VerboseNamePluralEnum
from products.models import Product
from services.models import Service
from users.models import Client, Provider, Manager


class Order(models.Model):
    state = models.CharField(max_length=32, choices=(
        (x.name, x.value) for x in StatusEnum
    ), verbose_name=VerboseNameEnum.STATE.value)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=VerboseNameEnum.CREATED_AT.value)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=VerboseNameEnum.UPDATED_AT.value)

    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, verbose_name=VerboseNameEnum.MANAGER.value)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name=VerboseNameEnum.CLIENT.value)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = VerboseNameEnum.ORDER.value
        verbose_name_plural = VerboseNamePluralEnum.ORDER.value


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=VerboseNameEnum.PRODUCT.value)
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        verbose_name=VerboseNameEnum.PROVIDER.value
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=VerboseNameEnum.ORDER.value)


    class Meta:
        verbose_name = VerboseNameEnum.ORDER_ITEM.value
        verbose_name_plural = VerboseNamePluralEnum.ORDER_ITEM.value


class ServiceOrder(models.Model):
    auto = models.CharField(max_length=64, verbose_name=VerboseNameEnum.AUTO.value)
    sale_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=VerboseNameEnum.SALE_PRICE.value)
    expenses = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=VerboseNameEnum.EXPENSES.value)

    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name=VerboseNameEnum.SERVICE.value)


    class Meta:
        verbose_name = VerboseNameEnum.SERVICE_ORDER.value
        verbose_name_plural = VerboseNamePluralEnum.SERVICE_ORDER.value
