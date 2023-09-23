#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Float
from sqlalchemy import create_engine, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60),
           ForeignKey('places.id',  onupdate="CASCADE", ondelete="CASCADE"),
           nullable=False, primary_key=True),
    Column('amenity_id', String(60),
           ForeignKey('amenities.id', onupdate="CASCADE", ondelete="CASCADE"),
           nullable=False, primary_key=True)
    )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    # for DBStorage
    #  relationship with the class Review
    reviews = relationship(
           'Review', backref='places', cascade='all, delete-orphan'
           )

    amenities = relationship(
            'Amenity', secondary=place_amenity,
            back_populates='place_amenities', viewonly=False
       )

    # for FileStorage
    @property
    def reviews(self):
        list_of_reviews = {}
        for review in storage.all(Review).values():
            if review.Place.id == self.id:
                list_of_reviews.append(review)
        return list_of_reviews
