#!/usr/bin/python3
"""Test for the Amenity """
import unittest
from os import getenv, remove
from models.base_model import BaseModel
from models.amenity import Amenity
import pep8

storage = getenv("HBNB_TYPE_STORAGE", "fs")


class TestAmenity(unittest.TestCase):
    """Test for the Amenity Class """
    @classmethod
    def setUpClass(cls):
        """Class setup for test"""
        cls.new_amenity = Amenity()
        cls.new_amenity.name = "Wifi"

    @classmethod
    def tearDownClass(cls):
        """TearDown Amenity unittest"""
        del cls.new_amenity
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_style_check(self):
        """Test the pep8 style guide"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "pep8 error needs fixing")

    def test_States_dbtable(self):
        """Test check for tablename correctness"""
        self.assertEqual(self.new_amenity.__tablename__, "amenities")

    def test_Amenity_inheritance(self):
        """Test check for inheritance from BaseModel"""
        self.assertIsInstance(self.new_amenity, BaseModel)

    def test_Amenity_attributes(self):
        """Test check for attribute Amenity"""
        self.assertTrue("name" in self.new_amenity.__dir__())

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_Amenity_attribute_type(self):
        """Test check for Amenity attribute types"""
        name_value = getattr(self.new_amenity, "name")
        self.assertIsInstance(name_value, str)
