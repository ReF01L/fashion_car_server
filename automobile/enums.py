from enum import Enum


class VerboseNameEnum(Enum):
    AUTO = 'Автомобиль'
    DRIVE = 'Вид привода'
    NAME = 'Название'
    YEAR = 'Год'
    RUDDER = 'Руль'


class VerboseNamePluralEnum(Enum):
    AUTO = 'Автомобили'


class RudderTypeEnum(Enum):
    RIGHT = 'Правый'
    LEFT = 'Левый'


class DriveEnum(Enum):
    FULL = 'Полный привод'
    BACK = 'Задний привод'
    FRONT = 'Передний привод'
