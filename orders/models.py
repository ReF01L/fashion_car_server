from django.db import models

from automobile.models import Auto
from orders.enums import StatusEnum, VerboseNameEnum, VerboseNamePluralEnum
from products.models import Product
from services.models import Service
from users.models import Client, Provider, Manager, Master


class Order(models.Model):
    state = models.CharField(max_length=32, choices=(
        (x.name, x.value) for x in StatusEnum
    ), verbose_name=VerboseNameEnum.STATE.value)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=VerboseNameEnum.CREATED_AT.value)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=VerboseNameEnum.UPDATED_AT.value)

    auto = models.ForeignKey(Auto, on_delete=models.SET_NULL, null=True, verbose_name=VerboseNameEnum.AUTO.value)

    manager = models.ForeignKey(
        Manager,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=VerboseNameEnum.MANAGER.value
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name=VerboseNameEnum.CLIENT.value
    )

    additional_expenses = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=VerboseNameEnum.ADDITIONAL_EXPENSES.value
    )

    description = models.TextField(verbose_name=VerboseNameEnum.DESCRIPTION.value)

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


class Sale(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=VerboseNameEnum.CREATED_AT.value)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=VerboseNameEnum.UPDATED_AT.value)

    auto = models.ForeignKey(Auto, on_delete=models.SET_NULL, null=True, verbose_name=VerboseNameEnum.AUTO.value)

    manager = models.ForeignKey(
        Manager,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=VerboseNameEnum.MANAGER.value
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name=VerboseNameEnum.CLIENT.value
    )

    description = models.TextField(verbose_name=VerboseNameEnum.DESCRIPTION.value)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = VerboseNameEnum.SALE.value
        verbose_name_plural = VerboseNamePluralEnum.SALE.value


class SaleItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=VerboseNameEnum.PRODUCT.value)
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        verbose_name=VerboseNameEnum.PROVIDER.value
    )
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, verbose_name=VerboseNameEnum.SALE.value)

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = VerboseNameEnum.SALE_ITEM.value
        verbose_name_plural = VerboseNamePluralEnum.SALE_ITEM.value


class ServiceOrder(models.Model):
    sale_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=VerboseNameEnum.SALE_PRICE.value)
    expenses = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=VerboseNameEnum.EXPENSES.value)

    state = models.CharField(max_length=32, choices=(
        (x.name, x.value) for x in StatusEnum
    ), default=StatusEnum.WAIT.name, verbose_name=VerboseNameEnum.STATE.value)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=VerboseNameEnum.CREATED_AT.value, null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=VerboseNameEnum.UPDATED_AT.value, null=True)

    master = models.ForeignKey(
        Master,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=VerboseNameEnum.MASTER.value
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name=VerboseNameEnum.CLIENT.value,
        null=True
    )

    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name=VerboseNameEnum.SERVICE.value)
    auto = models.ForeignKey(Auto, on_delete=models.SET_NULL, null=True, verbose_name=VerboseNameEnum.AUTO.value)

    description = models.TextField(verbose_name=VerboseNameEnum.DESCRIPTION.value)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = VerboseNameEnum.SERVICE_ORDER.value
        verbose_name_plural = VerboseNamePluralEnum.SERVICE_ORDER.value
