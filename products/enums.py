from enum import Enum


class VerboseNameEnum(Enum):
    UNUSED_PRODUCTS = 'Неиспользуемые товары'
    FOR_SUPPLY = 'Под поставку'
    SALE_PRICE = 'Цена продажи'
    PURCHASE_PRICE = 'Закупочная цена'
    AMOUNT = 'Количество'
    NAME = 'Название'
    PRODUCT = 'Продукт'
    CATEGORY = 'Категория'
    PRICE = 'Цена'


class VerboseNamePluralEnum(Enum):
    FOR_SUPPLY = 'Под поставку'
    PRODUCT = 'Продукты'
    CATEGORY = 'Категории'
    PRICE = 'Цены'


class UnusedProductsEnum(Enum):
    QUARTER_BY_3_MONTHS = '3 месяца'
    QUARTER_BY_6_MONTHS = '6 месяцев'
    QUARTER_BY_12_MONTHS = '12 месяцев'
