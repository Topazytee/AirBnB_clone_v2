#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import models


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        new_dict = {}
        if cls is None:
            return self.__objects
        if cls != "":
            for k, v in self.__objects.items():
                if cls == k.split(".")[0]:
                    new_dict[k] = v
            return new_dict
        else:
            return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        """Saves storage dictionary to file"""
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        """Deserialize json file"""
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val['__class__']
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object"""
        if obj is not None:
            key = str(obj.__class__.__name__) + "." + str(obj.id)
            FileStorage.__objects.pop(key, None)
            self.save()

    def close(self):
        """Deserializes JSON file to objects"""
        self.reload()
