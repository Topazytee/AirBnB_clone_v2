#!/usr/bin/python3
""" Module for testing file storage"""
import os
import time
import json
import unittest
import models
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage

db = os.getenv("HBNB_TYPE_STORAGE")


@unittest.skipIf(db == "db", "Testing DBstorage only")
class testFileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        self.storage = FileStorage()
        self.my_model = BaseModel()

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_all_return_type(self):
        """Test check for type return value"""
        storage_all = self.storage.all()
        self.assertIsInstance(storage_all, dict)

    def test_new_method(self):
        """Test check for new method"""
        self.storage.new(self.my_model)
        key = str(self.my_model.__class__.__name__ + "." + self.my_model.id)
        self.assertTrue(key in self.storage._FileStorage__objects)

    def test_objects_value_type(self):
        """Test check for value objects"""
        self.storage.new(self.my_model)
        key = str(self.my_model.__class__.__name__ + "." + self.my_model.id)
        val = self.storage._FileStorage__objects[key]
        self.assertIsInstance(self.my_model, type(val))

    def test_save_file_exists(self):
        """Test check for file.json"""
        self.storage.save()
        self.assertTrue(os.path.isfile('file.json'))

    def test_save_file_read(self):
        """Test check for file.json"""
        self.storage.save()
        self.storage.new(self.my_model)
        with open("file.json", encoding="UTF8") as fd:
            content = json.load(fd)
        self.assertTrue(type(content) is dict)

    def test_the_type_file_content(self):
        """Test check for file content"""
        self.storage.save()
        self.storage.new(self.my_model)
        with open("file.json", encoding="UTF8") as fd:
            content = fd.read()
        self.assertIsInstance(content, str)

    def test_reload_without_file(self):
        """Test check for no file"""
        try:
            self.storage.reload()
            self.assertTrue(True)
        except FileNotFoundError:
            self.assertTrue(False)

    def test_delete(self):
        """Test check for delete method"""
        fs = FileStorage()
        new_state = State()
        fs.new(new_state)
        state_id = new_state.id
        fs.save()
        fs.delete(new_state)
        with open("file.json", encoding="UTF-8") as fd:
            state_dict = json.load(fd)
        for k, v in state_dict.items():
            self.assertFalse(state_id == k.split('.')[1])

    def test_model_storage(self):
        """Test check for state model in FileStorage"""
        self.assertTrue(isinstance(storage, FileStorage))
