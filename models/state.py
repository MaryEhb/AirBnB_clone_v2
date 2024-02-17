#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """get cities  linked to state"""
            cities = []
            storage_cities = models.storage.all(City)
            for city in storage_cities.values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities

    def __init__(self, *args, **kwargs):
        """init state?"""
        super().__init__(*args, **kwargs)
