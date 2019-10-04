import enum


class UserType(enum.Enum):
    default = 'default'
    admin = 'admin'
    super_admin = 'super_admin'


class Manufacturer(enum.Enum):
    none = 'N/A'


class UOM(enum.Enum):
    none = 'N/A'
    tonnes = 'Tonnes'
    litre = 'Litre'
    kilogram = 'Kilogram'
    metre = 'Metre'
