#!/usr/bin/python3
"""user class inherits from base model"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Attributes:
        email (str): user mail
        password (str): password of the user.
        first_name (str): first name of the user.
        last_name (str): last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
