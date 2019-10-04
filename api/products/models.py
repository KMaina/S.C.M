from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.schema import Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ENUM

from helpers.database import Base
from utility.utility import Utility
from utility.enums import Manufacturer, UOM


class Product(Base, Utility):
    __tablename__ = 'products'
    id = Column(Integer, Sequence('products_id_seq'), primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    tax = Column(Float, nullable=False)
    manufacturer = Column(ENUM(Manufacturer, create_type=False), default='none')
    UOM = Column(ENUM(UOM, create_type=False), default='none')
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')

    def __init__(self, name, price, tax, manufacturer, UOM, user_id):
        self.name = name
        self.price = price
        self.tax = tax
        self.manufacturer = manufacturer
        self.uom = UOM
        self.user_id = user_id
