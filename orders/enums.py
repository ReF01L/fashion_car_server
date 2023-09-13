from enum import Enum


class StatusEnum(Enum):
    WAIT = 'Ожидание'
    PROGRESS = 'В процессе'
    READY = 'Готов'
    FINISHED = 'Выдан'


class VerboseNameEnum(Enum):
    DESCRIPTION = 'Описание'
    SALE_ITEM = 'Товар для продажи'
    SALE = 'Продажа'
    MASTER = 'Мастер'
    ADDITIONAL_EXPENSES = 'Дополнительные расходы'
    RESULT = 'Выручка'
    ORDER_ITEM = 'Элемент заказа'
    SERVICE_ORDER = 'Заказ услуги'
    SERVICE = 'Услуга'
    AUTO = 'Автомобиль'
    SALE_PRICE = 'Стоимость'
    EXPENSES = 'Расходы'
    STATE = 'Состояние'
    MANAGER = 'Менеджер'
    PRODUCT = 'Продукт'
    PROVIDER = 'Поставщик'
    CREATED_AT = 'Создан'
    UPDATED_AT = 'Последнее изменение'
    CLIENT = 'Клиент'
    ORDER = 'Заказ'


class VerboseNamePluralEnum(Enum):
    SALE_ITEM = 'Товары для продажи'
    SALE = 'Продажи'
    ORDER_ITEM = 'Элементы заказа'
    SERVICE_ORDER = 'Заказы услуг'
    ORDER = 'Заказы'