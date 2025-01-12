#!/usr/bin/python3
"""Define Amenity class that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ''
