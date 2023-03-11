#!/usr/bin/python3
""" this module defines the base model """
import uuid
import datetime
from engineimport storage

date_format = "%Y-%m-%dT%H:%M:%S.%f"
class BaseModel:
    """ defines all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        """ initializes base class """
        if kwargs:
            for key, value in kwargs.items():
                if key not in ["__class__", "created_at", "updated_at"]:
                    setattr(self, key, value)
            self.created_at = datetime.datetime.strptime(kwargs["created_at"], date_format)
            self.updated_at = datetime.datetime.strptime(kwargs["updated_at"], date_format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new()

    def __str__(self):
        """ returns the strung representation of basemodel"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute `updated_at`
        with the current datetime """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        to_dict = {key: value for key, value in self.__dict__.items() if key not in ["created_at", "updated_at"]}
        to_dict["__class__"] = type(self).__name__
        to_dict["created_at"] = self.created_at.isoformat()
        to_dict["updated_at"] = self.updated_at.isoformat()
        return to_dict

