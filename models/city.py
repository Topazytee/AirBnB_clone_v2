#!/usr/bin/python3
"""City Module for HBNB project"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """The city class, inherits from BaseModel"""
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", backref="cities",
                          cascade="all, delete, delete-orphan")
