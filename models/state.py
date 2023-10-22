#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
import os

from models.base_model import Base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':

        name = Column(String(128), nullable=False)
        cities = relationship('City', back_populates='state',
                              cascade='all, delete-orphan')
    else:

        @property
        def cities(self):
            """Returns the list of City instances
            with state_id equals to the current State.id
            """
            cities_lst = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_lst.append(city)
            return cities_lst
