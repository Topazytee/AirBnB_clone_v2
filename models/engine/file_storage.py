#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            return {key: obj for (key, obj) in self.__objects.items()
                    if isinstance(obj, cls)}
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        objects_dict = {}
        for key, val in self.__objects.items():
            objects_dict[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding="UTF-8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        """Deserialize json file"""
        try:
            with open(self.__file_path, encoding="UTF-8") as fd:
                for key, value in (json.load(fd)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if (key, obj) in self.__objects.items():
                self.__objects.pop(key, None)
        self.save()

    def close(self):
        """Deserializes JSON file to objects"""
        self.reload()

    def classes(self):
        """Return dict repr"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}
        return classes

    def attributes(self):
        """Returns valid attributes"""
        attributes = {"BaseModel": {"id": str,
                                    "created_at": datetime.datetime,
                                    "updated_at": datetime.datetime},
                      "User": {"email": str, "password": str,
                               "first_name": str, "last_name": str},
                      "State": {"name": str},
                      "City": {"state_id": str, "name": str},
                      "Amenity": {"name": str},
                      "Place": {"city_id": str, "user_id": str, "name": str,
                                "description": str, "number_rooms": int,
                                "number_bathrooms": int, "max_guest": int,
                                "price_by_night": int, "latitude": float,
                                "longitude": float, "amenity_ids": list},
                      "Review": {"place_id": str, "user_id": str, "text": str}
                      }
        return attributes
