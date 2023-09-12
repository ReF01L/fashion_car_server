from django.contrib import admin

from advanced_options.admin import AdvancedOptionProductInline
from products.filters import ProductUnusedFilter
from products.models import Product, Category, Price, ProductForSupply, ProductTuning, ProductTuningForSupply


class PriceInline(admin.TabularInline):
    model = Price
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'amount',
        'category',

        'sale_price',
        'purchase_price',
        'margin',
        'result',
        'sells',
    )
    inlines = (PriceInline, AdvancedOptionProductInline)
    list_filter = (ProductUnusedFilter,)
    exclude = ('advanced_options',)

    def get_queryset(self, request):
        category, _ = Category.objects.get_or_create(
            name='Тюнинг',
            defaults={'name': 'Тюнинг'}
        )
        return super().get_queryset(request).filter(
            for_supply=False
        ).exclude(category=category)

    @admin.display(empty_value='Не указано', description='Закупочная цена')
    def sale_price(self, product: Product):
        if hasattr(product, 'price'):
            return str(product.price.sale_price)

    @admin.display(empty_value='Не указано', description='Цена продажи')
    def purchase_price(self, product: Product):
        if hasattr(product, 'price'):
            return str(product.price.purchase_price)

    @admin.display(empty_value='Не указано', description='Выручка')
    def result(self, product: Product):
        if hasattr(product, 'price'):
            return f'{product.price.sale_price - product.price.purchase_price}'

    @admin.display(empty_value='Цена не указана', description='Маржа')
    def margin(self, product: Product):
        if hasattr(product, 'price'):
            return '{:.2f}%'.format(
                (product.price.sale_price - product.price.purchase_price) / product.price.sale_price * 100)

    @admin.display(description='Товара продано')
    def sells(self, product: Product):
        return product.orderitem_set.all().count()


@admin.register(ProductForSupply)
class ProductForSupplyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'amount',
        'category',

        'sale_price',
        'purchase_price',
        'margin',
        'result',
        'sells',
    )
    inlines = (PriceInline, AdvancedOptionProductInline)
    list_filter = (ProductUnusedFilter,)
    exclude = ('advanced_options',)

    def get_queryset(self, request):
        category, _ = Category.objects.get_or_create(
            name='Тюнинг',
            defaults={'name': 'Тюнинг'}
        )
        return super().get_queryset(request).filter(
            for_supply=False
        ).exclude(category=category)

    @admin.display(empty_value='Не указано', description='Закупочная цена')
    def sale_price(self, product: Product):
        if hasattr(product, 'price'):
            return str(product.price.sale_price)

    @admin.display(empty_value='Не указано', description='Цена продажи')
    def purchase_price(self, product: Product):
        if hasattr(product, 'price'):
            return str(product.price.purchase_price)

    @admin.display(empty_value='Не указано', description='Выручка')
    def result(self, product: Product):
        if hasattr(product, 'price'):
            return f'{product.price.sale_price - product.price.purchase_price}'

    @admin.display(empty_value='Цена не указана', description='Маржа')
    def margin(self, product: Product):
        if hasattr(product, 'price'):
            return '{:.2f}%'.format(
                (product.price.sale_price - product.price.purchase_price) / product.price.sale_price * 100)

    @admin.display(description='Товара продано')
    def sells(self, product: Product):
        return product.orderitem_set.all().count()


@admin.register(ProductTuning)
class ProductTuningAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'amount',
        'category',

        'sale_price',
        'purchase_price',
        'margin',
        'result',
        'sells',
    )
    inlines = (PriceInline, AdvancedOptionProductInline)
    list_filter = (ProductUnusedFilter,)
    exclude = ('advanced_options',)

    def get_queryset(self, request):
        category, _ = Category.objects.get_or_create(
            name='Тюнинг',
            defaults={'name': 'Тюнинг'}
        )
        return super().get_queryset(request).filter(
            for_supply=False,
            category=category
        )

    @admin.display(empty_value='Не указано', description='Закупочная цена')
    def sale_price(self, product: Product):
        if hasattr(product, 'price'):
            return str(product.price.sale_price)

    @admin.display(empty_value='Не указано', description='Цена продажи')
    def purchase_price(self, product: Product):
        if hasattr(product, 'price'):
            return str(product.price.purchase_price)

    @admin.display(empty_value='Не указано', description='Выручка')
    def result(self, product: Product):
        if hasattr(product, 'price'):
            return f'{product.price.sale_price - product.price.purchase_price}'

    @admin.display(empty_value='Цена не указана', description='Маржа')
    def margin(self, product: Product):
        if hasattr(product, 'price'):
            return '{:.2f}%'.format(
                (product.price.sale_price - product.price.purchase_price) / product.price.sale_price * 100)

    @admin.display(description='Товара продано')
    def sells(self, product: Product):
        return product.orderitem_set.all().count()


@admin.register(ProductTuningForSupply)
class ProductTuningForSupplyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'amount',
        'category',

        'sale_price',
        'purchase_price',
        'margin',
        'result',
        'sells',
    )
    inlines = (PriceInline, AdvancedOptionProductInline)
    list_filter = (ProductUnusedFilter,)
    exclude = ('advanced_options',)

    def get_queryset(self, request):
        category, _ = Category.objects.get_or_create(
            name='Тюнинг',
            defaults={'name': 'Тюнинг'}
        )
        return super().get_queryset(request).filter(
            for_supply=True,
            category=category
        )

    @admin.display(empty_value='Не указано', description='Закупочная цена')
    def sale_price(self, product: Product):
        if hasattr(product, 'price'):
            return str(product.price.sale_price)

    @admin.display(empty_value='Не указано', description='Цена продажи')
    def purchase_price(self, product: Product):
        if hasattr(product, 'price'):
            return str(product.price.purchase_price)

    @admin.display(empty_value='Не указано', description='Выручка')
    def result(self, product: Product):
        if hasattr(product, 'price'):
            return f'{product.price.sale_price - product.price.purchase_price}'

    @admin.display(empty_value='Цена не указана', description='Маржа')
    def margin(self, product: Product):
        if hasattr(product, 'price'):
            return '{:.2f}%'.format(
                (product.price.sale_price - product.price.purchase_price) / product.price.sale_price * 100)

    @admin.display(description='Товара продано')
    def sells(self, product: Product):
        return product.orderitem_set.all().count()


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
