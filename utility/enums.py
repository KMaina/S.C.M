import enum


class UserType(enum.Enum):
    default = 'default'
    admin = 'admin'
    super_admin = 'super_admin'
