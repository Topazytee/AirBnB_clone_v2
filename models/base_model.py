#!/usr/bin/python3
"""BaseModel Module"""
from os import getenv
import uuid
from datetime import datetime
import models
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """A base class for all other models"""
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes a new model instance attribute"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs.keys():
                setattr(self, "id", str(uuid.uuid4()))
            time = datetime.now()
            if "created_at" not in kwargs.keys():
                setattr(self, "created_at", time)
            if "updated_at" not in kwargs.keys():
                setattr(self, "updated_at", time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        dic = self.to_dict()
        return ("[{}] ({}) {}".format(type(self).__name__, self.id,
                                      dic))

    def __repr__(self):
        """Return string representation of the BaseModel class"""
        return self.__str__()

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance of BaseModel into dict format representation"""
        cp_dct = self.__dict__.copy()
        cp_dct['__class__'] = type(self).__name__
        cp_dct['created_at'] = cp_dct["created_at"].isoformat()
        cp_dct['updated_at'] = cp_dct["updated_at"].isoformat()
        if '_sa_instance_state' in cp_dct.keys():
            cp_dct.pop('_sa_instance_state', None)
        return cp_dct

    def delete(self):
        """Delete object"""
        models.storage.delete(self)
