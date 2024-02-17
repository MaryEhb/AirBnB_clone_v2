#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all')
    else:
        name = ""

        def cities(self):
            """get cities  linked to state"""
            cities = []
            cities_dict = storage.all(models.City)
            for key, value in cities_dict.items():
                if self.id == value.state_id:
                    cities.append(value)
            return cities
