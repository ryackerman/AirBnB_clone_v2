#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import os
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # For DBStorage: create relationship with the class City
    cities = relationship(
                    'City', backref='state', cascade='all, delete-orphan')

    @property
    def cities(self):
        list_of_cities = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                list_of_cities.append(city)
        return list_of_cities
