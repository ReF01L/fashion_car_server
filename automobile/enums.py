from enum import Enum


class VerboseNameEnum(Enum):
    DRIVE = 'Вид привода'
    NAME = 'Название'
    YEAR = 'Год'
    RUDDER = 'Руль'


class VerboseNamePluralEnum(Enum):
    pass


class RudderTypeEnum(Enum):
    RIGHT = 'Правый'
    LEFT = 'Левый'


class DriveEnum(Enum):
    FULL = 'Полный привод'
    BACK = 'Задний привод'
    FRONT = 'Передний привод'
