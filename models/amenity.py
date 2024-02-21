#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import uuid
import models
from datetime import datetime
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DATETIME
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ The Amenity Class"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    def __init__(self, *args, **kwargs):
        """initializing Amenity"""
        super().__init__(*args, **kwargs)
