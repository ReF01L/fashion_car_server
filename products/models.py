from django.db import models

from products.enums import VerboseNameEnum, VerboseNamePluralEnum


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name=VerboseNameEnum.NAME.value)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = VerboseNameEnum.CATEGORY.value
        verbose_name_plural = VerboseNamePluralEnum.CATEGORY.value


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name=VerboseNameEnum.NAME.value)
    amount = models.PositiveIntegerField(verbose_name=VerboseNameEnum.AMOUNT.value)
    for_supply = models.BooleanField(verbose_name=VerboseNameEnum.FOR_SUPPLY.value)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=VerboseNameEnum.CATEGORY.value)

    def __str__(self) -> str:
        return self.name

    def sell(self, count: int = 1) -> int:
        update_fields = ['amount']

        self.amount -= count

        if self.amount == 0:
            self.for_supply = True
            update_fields.append('for_supply')

        self.save(update_fields=update_fields)

        return self.amount

    def increased(self, count: int = 1) -> int:
        self.amount += count
        self.save(update_fields=('amount',))

        return self.amount

    class Meta:
        verbose_name = VerboseNameEnum.PRODUCT.value
        verbose_name_plural = VerboseNamePluralEnum.PRODUCT.value


class ProductForSupply(Product):
    class Meta:
        proxy = True
        verbose_name = VerboseNameEnum.FOR_SUPPLY.value
        verbose_name_plural = VerboseNamePluralEnum.FOR_SUPPLY.value


class Price(models.Model):
    purchase_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=VerboseNameEnum.PURCHASE_PRICE.value
    )
    sale_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=VerboseNameEnum.SALE_PRICE.value)

    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self) -> str:
        return f'{self.product.name}'

    class Meta:
        verbose_name = VerboseNameEnum.PRICE.value
        verbose_name_plural = VerboseNamePluralEnum.PRICE.value
