from enum import Enum


class VerboseNameEnum(Enum):
    UPDATED_AT = 'Последнее обновление'
    CREATED_AT = 'Создано'
    ADVERTISING = 'Реклама'
    EXPENSES = 'Затраты'
    NAME = 'Название'


class VerboseNamePluralEnum(Enum):
    ADVERTISING = 'Реклама'
