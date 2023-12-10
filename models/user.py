#!/usr/bin/python3
"""This module stores the User class """
from models.base_model import BaseModel


class User(BaseModel):
    """This class stores the User data"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
