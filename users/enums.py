from enum import Enum


class VerboseNameEnum(Enum):
    USER = 'Пользователь'
    TOTAL_SALARY = 'Зарплата'
    PROVIDER = 'Поставщик'
    ADDITIONAL_PERCENT = 'Процент от прибыли'
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
    USER = 'Пользователи'
    PROVIDER = 'Поставщики'
    MASTER = 'Мастер'
    CLIENT = 'Клиенты'
    MANAGER = 'Менеджеры'