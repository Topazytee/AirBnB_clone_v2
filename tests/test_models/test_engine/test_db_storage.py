#!/usr/bin/python3
""" Module for testing file storage"""
import time
import unittest
import sys
from models.engine.db_storage import DBStorage
from models import storage
from models.user import User
from models.state import State
from console import HBNBCommand
from os import getenv
from io import StringIO

db = getenv("HBNB_TYPE_STORAGE")


@unittest.skipIf(db != "db", "Testing DBstorage only")
class test_DBStorage(unittest.TestCase):
    """ Class to test the DB_ storage method """

    @classmethod
    def setUpClass(cls):
        """ Set up test environment """
        cls.dbstorage = DBStorage()
        cls.output = StringIO()
        sys.stdout = cls.output

    @classmethod
    def tearDownClass(cls):
        """ Remove storage file at end of tests """
        del cls.dbstorage
        del cls.output

    def create(self):
        """Create HBNBCommand()"""
        return HBNBCommand()

    def test_new(self):
        """Test check for new DB"""
        new_obj = State(name="California")
        self.assertEqual(new_obj.name, "California")

    def test_dbstorage_user_attr(self):
        """Test check for attr"""
        new = User(emaiil="Gail@hbtn.com", password="hello")
        self.assertTrue(new.email, "Gail@hbtn.com")

    def test_dbstorage_check_method(self):
        """Test check for method"""
        self.assertTrue(hasattr(self.dbstorage, "all"))
        self.assertTrue(hasattr(self.dbstorage, "__init__"))
        self.assertTrue(hasattr(self.dbstorage, "new"))
        self.assertTrue(hasattr(self.dbstorage, "save"))
        self.assertTrue(hasattr(self.dbstorage, "delete"))
        self.assertTrue(hasattr(self.dbstorage, "reload"))

    def test_dbstorage_all(self):
        """Test check for all functions"""
        storage.reload()
        result = storage.all("")
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 0)
        new = User(email="Xavi@hbtn.com", password="abc")
        console = self.create()
        console.onecmd("create State name=California")
        result = storage.all("State")
        self.assertTrue(len(result) > 0)

    def test_dbstorage_new_save(self):
        """Test check for save"""
        new_state = State(name="New York")
        storage.new(new_state)
        save_id = new_state.id
        result = storage.all("State")
        temp_list = []
        for k, v in result.items():
            temp_list.append(k.split('.')[1])
            obj = v
        self.assertTrue(save_id in temp_list)
        self.assertIsInstance(obj, State)

    def test_dbstorage_delete(self):
        """Test check for delete method"""
        new_user = User(email="aol@yahoo.com", password="abc",
                        first_name="Abigail", last_name="Hindly")
        storage.new(new_user)
        save_id = new_user.id
        key = "User.{}".format(save_id)
        self.assertIsInstance(new_user, User)
        storage.save()
        old_result = storage.all("User")
        del_user_obj = old_result[key]
        storage.delete(del_user_obj)
        new_result = storage.all("User")
        self.assertNotEqual(len(old_result), len(new_result))

    def test_model_storage(self):
        """Test check for state model in DBStorage"""
        self.assertTrue(isinstance(storage, DBStorage))
