#!/usr/bin/python3
""" holds class User"""
import hashlib
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a user"""
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        _password = Column("password", String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        _password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes user with hashed password"""
        super().__init__(*args, **kwargs)
        if "password" in kwargs:
            self.password = kwargs["password"]

    @staticmethod
    def hash_password(password):
        """Hashes a password using MD5"""
        return hashlib.md5(password.encode()).hexdigest()

    @property
    def password(self):
        """Getter for password (not recommended for real-world use)"""
        return self._password

    @password.setter
    def password(self, value):
        """Hashes password when setting it"""
        self._password = self.hash_password(value)
