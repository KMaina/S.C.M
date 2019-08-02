from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import Sequence

from helpers.database import Base
from utility.utility import Utility


class User(Base, Utility):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('users_id_seq'), primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)

    # __table_args__ = (
    #     Index(
    #     'ix_users_index',
    #     'name',
    #     unique=True)
    # )

    def __init__(self, name, password):
        self.name = name
        self.password = password
