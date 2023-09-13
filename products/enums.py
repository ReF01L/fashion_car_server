from enum import Enum


class VerboseNameEnum(Enum):
    DESCRIPTION = 'Описание'
    TUNING_FOR_SUPPLY = 'Тюнинг под заказ'
    TUNING = 'Тюнинг в наличии'
    UNUSED_PRODUCTS = 'Неиспользуемые товары'
    FOR_SUPPLY = 'Под поставку'
    SALE_PRICE = 'Цена продажи'
    PURCHASE_PRICE = 'Закупочная цена'
    AMOUNT = 'Количество'
    NAME = 'Название'
    PRODUCT = 'Товар'
    CATEGORY = 'Категория'
    PRICE = 'Цена'


class VerboseNamePluralEnum(Enum):
    PRODUCT_TITLE = 'Товары'
    TUNING_FOR_SUPPLY = 'Тюнинг под заказ'
    TUNING = 'Тюнинг в наличии'
    FOR_SUPPLY = 'Аксессуары под заказ'
    PRODUCT = 'Аксессуары в наличии'
    CATEGORY = 'Категории'
    PRICE = 'Цены'


class UnusedProductsEnum(Enum):
    QUARTER_BY_3_MONTHS = '3 месяца'
    QUARTER_BY_6_MONTHS = '6 месяцев'
    QUARTER_BY_12_MONTHS = '12 месяцев'
