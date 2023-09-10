from django.apps import AppConfig

from products.enums import VerboseNamePluralEnum


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
    verbose_name = VerboseNamePluralEnum.PRODUCT.value
