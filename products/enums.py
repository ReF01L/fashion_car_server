from enum import Enum


class VerboseNameEnum(Enum):
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
