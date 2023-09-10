from enum import Enum


class VerboseNameEnum(Enum):
    PROVIDER = 'Поставщик'
    ADDITIONAL_PERCENT = 'Процент от продаж'
    SALARY = 'Оклад'
    MASTER = 'Мастер'
    USER_NAME = 'Имя'
    SECOND_NAME = 'Фамилия'
    PATRONYMIC = 'Отчество'
    PHONE = 'Номер телефона'
    IS_ACTIVE = 'Активен'
    IS_STAFF = 'Сотрудник'
    IS_SUPERUSER = 'Суперпользователь'
    CREATED_AT = 'Создан'
    UPDATED_AT = 'Последнее изменение'
    MANAGER = 'Менеджер'
    CLIENT = 'Клиент'


class VerboseNamePluralEnum(Enum):
    PROVIDER = 'Поставщики'
    MASTER = 'Мастер'
    CLIENT = 'Клиенты'
    MANAGER = 'Менеджеры'