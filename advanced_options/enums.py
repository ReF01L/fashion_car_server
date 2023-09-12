from enum import Enum


class VerboseNameEnum(Enum):
    VALUE = 'Значение'
    KEY = 'Опция'
    ADVANCED_OPTION = 'Описание'


class VerboseNamePluralEnum(Enum):
    PRODUCT_OPTION = 'Описание товара'
    ORDER_SERVICE_OPTION = 'Описание услуги'
    ORDER_OPTION = 'Описание заказа'
    ADVANCED_OPTION = 'Описания'
