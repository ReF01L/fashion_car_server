from django.contrib import admin

from products.filters import ProductUnusedFilter
from products.models import Product, Category, Price, ProductForSupply


class PriceInline(admin.TabularInline):
    model = Price


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
    )
    inlines = (PriceInline,)
    list_filter = (ProductUnusedFilter,)

    def get_queryset(self, request):
        return super().get_queryset(request).filter(
            for_supply=False
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


@admin.register(ProductForSupply)
class ProductForSupplyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'amount',
        'category',

        'sale_price',
        'purchase_price',
        'margin'
    )
    inlines = (PriceInline,)

    def get_queryset(self, request):
        return super().get_queryset(request).filter(
            for_supply=True
        )

    @admin.display(empty_value='Не указано', description='Закупочная цена')
    def sale_price(self, product: Product):
        if hasattr(product, 'price'):
            return str(product.price.sale_price)

    @admin.display(empty_value='Не указано', description='Цена продажи')
    def purchase_price(self, product: Product):
        if hasattr(product, 'price'):
            return str(product.price.purchase_price)

    @admin.display(empty_value='Цена не указана', description='Маржа')
    def margin(self, product: Product):
        if hasattr(product, 'price'):
            return '{:.2f}%'.format(
                (product.price.sale_price - product.price.purchase_price) / product.price.sale_price * 100)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

# @admin.register(Price)
# class PriceAdmin(admin.ModelAdmin):
#     list_display = (
#         'product',
#         'purchase_price',
#         'sale_price',
#
#         'result_price'
#     )
#
#     @admin.display(description='Заработок компании')
#     def result_price(self, price: Price):
#         return price.sale_price - price.purchase_price
