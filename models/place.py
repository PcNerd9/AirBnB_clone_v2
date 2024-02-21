#!/usr/bin/python3
""" Place Module for HBNB project """
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), default='')
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, default=0)
    longitude = Column(Float, default=0)
    amenity_ids = []
    
    
    place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False), 
    extend_existing=True
    )

    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', back_populates='place', cascade='all, delete')
        amenities = relationship('Amenity', secondary='place_amenity', viewonly=False)
    else:
        @property
        def reviews(self):
            from models.review import Review
            result = []
            for values in models.storage.all(Review).values():
                result.append(values)
            return result
        @property
        def amenities(self):
            """ Getter attribute that returns list of Amenity instances """
            from models import storage
            amenity_list = []
            for amenity_id in self.amenity_ids:
                amenity = storage.get('Amenity', amenity_id)
                if amenity:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, obj):
            """ Setter attribute that handles adding Amenity.id to amenity_ids """
            if obj.__class__.__name__ == 'Amenity':
                self.amenity_ids.append(obj.id)

    amenities = relationship('Amenity', secondary='place_amenity')

#Creating the association table
