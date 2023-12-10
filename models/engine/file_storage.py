#!/usr/bin/python3
"""This module stores the FileStorage class"""

from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
import json
import os.path


class FileStorage:
    """
    This class serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns __objects"""
        return FileStorage.__objects

    def to_dict(self):
        """returns __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets __objects to given obj"""
        id = obj.to_dict()["id"]
        classname = obj.to_dict()["__class__"]
        keyName = classname + "." + id
        FileStorage.__objects[keyName] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        filepath = FileStorage.__file_path
        data = dict(FileStorage.__objects)
        for key, value in data.items():
            data[key] = value.to_dict()
        with open(filepath, 'w') as f:
            json.dump(data, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        filepath = FileStorage.__file_path
        data = FileStorage.__objects
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r') as f:
                    for key, value in json.load(f).items():
                        if "BaseModel" in key:
                            data[key] = BaseModel(**value)
                        if "User" in key:
                            data[key] = User(**value)
                        if "State" in key:
                            data[key] = State(**value)
                        if "City" in key:
                            data[key] = City(**value)
                        if "Amenity" in key:
                            data[key] = Amenity(**value)
                        if "Place" in key:
                            data[key] = Place(**value)
                        if "Review" in key:
                            data[key] = Review(**value)
            except Exception:
                pass
