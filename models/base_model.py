#!/usr/bin/python3
'''Defines the BaseModel class'''

import models
from uuid import uuid4
from datetime import datetime


class BaseModel():
    '''BaseModel class'''
    def __init__(self, *args, **kwargs):
        '''Initialize a new BaseModel'''
        timefmt = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, timefmt)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        '''returns the string representation of the BaseModel instance'''
        className = self.__class__.__name__
        return ("[{}] ({}) {}".format(className, self.id, self.__dict__))

    def save(self):
        '''updates the public instance attribute
        updated_at with the current datetime'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''returns a dictionary containing all keys/values
        of the BaseModel instance'''
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return (obj_dict)
