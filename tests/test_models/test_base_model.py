#!/usr/bin/python3
"""Test for BaseModel """

import unittest
import sys
import datetime
from models.base_model import BaseModel
from io import StringIO
from os import getenv

storage = getenv("HBNB_TYPE_STORAGE", "fs")


class TestBase(unittest.TestCase):
    """Class test for BaseModel"""
    def setUp(self):
        """Initialize instance"""
        self.my_model = BaseModel()
        self.my_model.name = "Liz Benson"
        self.new = BaseModel()

    def tearDown(self):
        """Teardown for class"""
        del self.my_model

    def test_id_type(self):
        """Test check for id is string"""
        self.assertEqual("<class 'str'>", str(type(self.my_model.id)))

    def test_ids_differs(self):
        """Test check for different id between instances"""
        new_model = BaseModel()
        self.assertNotEqual(new_model.id, self.my_model.id)

    def test_name(self):
        """Test check for attribute to be added"""
        self.assertEqual("Liz Benson", self.my_model.name)

    def test_a_updated_created_equal(self):
        """Test check for date equality"""
        self.assertEqual(self.my_model.updated_at.year,
                         self.my_model.created_at.year)

    def test_str_overide(self):
        """Test check for message"""
        backup = sys.stdout
        inst_id = self.my_model.id
        capture_out = StringIO()
        sys.stdout = capture_out
        print(self.my_model)

        cap = capture_out.getvalue().split(" ")
        self.assertEqual(cap[0], "[BaseModel]")

        self.assertEqual(cap[1], "({})".format(inst_id))
        sys.stdout = backup

    def test_to_dict_type(self):
        """Test check for dictionay method"""
        self.assertEqual("<class 'dict'>", str(type(self.my_model.to_dict())))

    def test_to_dict_class(self):
        """Test check for __class__"""
        self.assertEqual("BaseModel", (self.my_model.to_dict())["__class__"])

    def test_to_dict_type_updated_at(self):
        """Test check for value updated_at"""
        self.assertEqual("<class 'str'>", str(type((
            self.my_model.to_dict())["updated_at"])))

    def test_to_dict_type_created_at(self):
        """Test check for value created_at"""
        temp = self.my_model.to_dict()
        self.assertEqual("<class 'str'>", str(type(temp["created_at"])))

    def test_kwargs_instantiation(self):
        """Test check for instance creation"""
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        self.assertEqual(new_model.id, self.my_model.id)

    def test_type_created_at(self):
        """Test check for new model update"""
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertTrue(isinstance(new_model.created_at, datetime.datetime))

    def test_type_updated_at(self):
        """Test check for new model created_at"""
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertTrue(isinstance(new_model.updated_at, datetime.datetime))

    def test_compare_dict(self):
        """Test check for equality new_model and my_model"""
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        new_model_dict = new_model.to_dict()
        self.assertEqual(my_model_dict, new_model_dict)

    def test_instance_diff(self):
        """Test check for inequality new_model and my_model"""
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertNotEqual(self.my_model, new_model)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_save(self):
        """Test check for difference after updates"""
        old_update = self.new.updated_at
        self.new.save()
        self.assertNotEqual(self.new.updated_at, old_update)

    @unittest.skipIf(storage != "db", "Testing if using DBStorage")
    def test_basemodel_hasattr(self):
        """Test check for class attribute"""
        self.assertTrue(hasattr(self.new, "id"))
        self.assertTrue(hasattr(self.new, "created_at"))
        self.assertTrue(hasattr(self.new, "updated_at"))

    @unittest.skipIf(storage != "db", "Testing if using DBStorage")
    def test_basemodel_attrtype(self):
        """Test check for attribute type"""
        new2 = BaseModel
        self.assertFalse(isinstance(new2.id, str))
        self.assertFalse(isinstance(new2.created_at, str))
        self.assertFalse(isinstance(new2.updated_at, str))
