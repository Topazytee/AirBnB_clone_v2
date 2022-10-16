#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import datetime
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        """Init method"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            objs = self.__session.query(self.classes()[cls])
        else:
            objs = self.__session.query(State).all()
            objs += self.__session.query(City).all()
            objs += self.__session.query(User).all()
            objs += self.__session.query(Place).all()
            objs += self.__session.query(Amenity).all()
            objs += self.__session.query(Review).all()

        dic = {}
        for obj in objs:
            k = '{}.{}'.format(type(obj).__name__, obj.id)
            dic[k] = obj
        return dic

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """Saves storage dictionary to file"""
        self.__session.commit()

    def delete(self):
        """Delete occurrence"""
        self.__session.delete(obj)

    def reload(self):
        """Create occurrence"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()

    def close(self):
        """Removes database"""
        self.__session.remove()

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
