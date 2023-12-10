#!/usr/bin/python3
"""This module stores the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class stores the Review data"""
    place_id = ""
    user_id = ""
    text = ""
