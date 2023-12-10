#!/usr/bin/python3
"""
class BaseModel defines all common attributes/methods for other classes
for all models in our hbnb clone
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    A base class for all hbnb models
    """

    def __init__(self, *args, **kwargs) -> None:
        """Initialization of BaseModel Class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self) -> str:
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self) -> None:
        """Update the public instance attribute updated_at with the current
        datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """
        Return a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        todict = dict(self.__dict__)
        todict = self.__dict__.copy()
        todict["__class__"] = self.__class__.__name__
        if not isinstance(todict["created_at"], str):
            todict["created_at"] = self.created_at.isoformat()
        if not isinstance(todict["updated_at"], str):
            todict["updated_at"] = self.updated_at.isoformat()
        return todict
