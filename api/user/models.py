from werkzeug.security import generate_password_hash

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.schema import Sequence

from helpers.database import Base
from utility.utility import Utility
from utility.enums import UserType


class User(Base, Utility):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('users_id_seq'), primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    user_type = Column(Enum(UserType), default='default')

    def __init__(self, name, password, user_type):
        self.name = name
        self.password = generate_password_hash(password,
                                               method='pbkdf2:sha256',
                                               salt_length=12)
        self.user_type = user_type
