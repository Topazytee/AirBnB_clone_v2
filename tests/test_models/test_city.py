#!/usr/bin/python3
"""Test check for City"""

import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from os import getenv, remove

storage = getenv("HBNB_TYPE_STORAGE", "fs")


class TestCity(unittest.TestCase):
    """Test check for City class"""
    @classmethod
    def setUpClass(cls):
        """Set up unittest check for class City"""
        cls.new_city = City()
        cls.new_city.state_id = "California"
        cls.new_city.name_id = "San Francisco"

    @classmethod
    def tearDownClass(cls):
        """Tear down unittest"""
        del cls.new_city
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_City_dbtable(self):
        """Test check for table correctness"""
        self.assertEqual(self.new_city.__tablename__, "cities")

    def test_City_inheritance(self):
        """Test check for inheritance from BaseModel"""
        self.assertIsInstance(self.new_city, BaseModel)

    def test_City_attributes(self):
        """Test check for city attributes"""
        self.assertTrue("state_id" in self.new_city.__dir__())
        self.assertTrue("name" in self.new_city.__dir__())

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_name(self):
        """Test check for name type"""
        name = getattr(self.new_city, "name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_name(self):
        """Test check for name type"""
        name = getattr(self.new_city, "state_id")
        self.assertIsInstance(name, str)
