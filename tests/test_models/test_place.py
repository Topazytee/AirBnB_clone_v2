#!/usr/bin/python3
"""Test check for Place"""

import unittest
from models.base_model import BaseModel
from models.place import Place
from os import getenv, remove

storage = getenv("HBNB_TYPE_STORAGE", "fs")


class TestPlace(unittest.TestCase):
    """Test check for Place class"""
    @classmethod
    def setUpClass(cls):
        """Set up unittest"""
        cls.new_place = Place(city_id="0O01", user_id="0O02", name="house",
                              description="awesome", number_rooms=3,
                              number_bathrooms=2, max_guest=1,
                              price_by_night=100, latitude=37.77,
                              longitude=127.12)

    @classmethod
    def teardownClass(cls):
        """Test check to tear down unittest"""
        del cls.new_place
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_Place_dbtable(self):
        """Test check for table name correctness"""
        self.assertEqual(self.new_place.__tablename__, "places")

    def test_Place_inheritance(self):
        """Test check for inheritance from BaseModel"""
        self.assertIsInstance(self.new_place, BaseModel)

    def test_Place_attributes(self):
        """Test check for attributes"""
        self.assertTrue('city_id' in self.new_place.__dir__())
        self.assertTrue('user_id' in self.new_place.__dir__())
        self.assertTrue('description' in self.new_place.__dir__())
        self.assertTrue('name' in self.new_place.__dir__())
        self.assertTrue('number_rooms' in self.new_place.__dir__())
        self.assertTrue('max_guest' in self.new_place.__dir__())
        self.assertTrue('price_by_night' in self.new_place.__dir__())
        self.assertTrue('latitude' in self.new_place.__dir__())
        self.assertTrue('longitude' in self.new_place.__dict__())

    @unittest.skipIf(storage == "db", "Testing database for storage only")
    def test_place_amenity_attrb(self):
        """Test check for amenity place"""
        self.assertTrue("amenity_ids" in self.new_place.__dir__())

    @unittest.skipIf(storage == "db", "Testing database for storage only")
    def test_place_amenity_dbattrb(self):
        """Test check for db attribute amenity"""
        self.assertTrue("amenities" in self.new_place.__dir__())
        self.assertTrue("reviews" in self.new_place.__dir__())

    @unittest.skipIf(storage == "db", "Testing database for storage only")
    def test_type_longitude(self):
        """Test check for type longitude"""
        longitude = getattr(self.new_place, "longitude")
        self.assertIsInstance(longitude, float)

    @unittest.skipIf(storage == "db", "Testing database for storage only")
    def test_type_latitude(self):
        """Test check for type latitude"""
        latitude = getattr(self.new_place, "latitude")
        self.assertIsInstance(latitude, float)

    @unittest.skipIf(storage == "db", "Testing database for storage only")
    def test_type_amenity(self):
        """Test check for type amenity"""
        amenity = getattr(self.new_place, "amenity-ids")
        self.assertIsInstance(amenity, list)

    @unittest.skipIf(storage == "db", "Testing database for storage only")
    def test_type_price_by_night(self):
        """Test check for type price_by_night"""
        price_by_night = getattr(self.new_place, "price_by_night")
        self.assertIsInstance(price_by_night, int)

    @unittest.skipIf(storage == "db", "Testing database for storage only")
    def test_type_max_guest(self):
        """Test check for type max_guest"""
        max_guest = getattr(self.new_place, "max_guest")
        self.assertIsInstance(max_guest, int)

    @unittest.skipIf(storage == "db", "Testing database for storage only")
    def test_type_number_bathrooms(self):
        """Test check for type number_bathrooms"""
        number_bathrooms = getattr(self.new_place, "number_bathrooms")
        self.assertIsInstance(number_bathrooms, int)

    @unittest.skipIf(storage == "db", "Testing database for storage only")
    def test_type_number_rooms(self):
        """Test check for type number_rooms"""
        number_rooms = getattr(self.new_place, "number_rooms")
        self.assertIsInstance(number_rooms, int)

    @unittest.skipIf(storage == "db", "Testing database for storage only")
    def test_type_description(self):
        """Test check for type description"""
        description = getattr(self.new_place, "description")
        self.assertIsInstance(description, str)

    @unittest.skipIf(storage == "db", "Testing database for storage only")
    def test_type_name(self):
        """Test check for type name"""
        name = getattr(self.new_place, "name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(storage == "db", "Testing database for storage only")
    def test_type_user_id(self):
        """Test check for type user_id"""
        user_id = getattr(self.new_place, "user_id")
        self.assertIsInstance(user_id, str)

    @unittest.skipIf(storage == "db", "Testing database for storage only")
    def test_type_city_id(self):
        """Test check for type city_id"""
        city_id = getattr(self.new_place, "city_id")
        self.assertIsInstance(city_id, str)
