#!/usr/bin/python3
"""Test check for User"""

import unittest
from models.base_model import BaseModel
from models.user import User
from os import getenv, remove
from io import StringIO
import sys
import datetime
import pep8

storagge = getenv("HBNB_TYPE_STORAGE", "fs")


class TestUser(unittest.TestCase):
    """Test check for User class"""
    @classmethod
    def setUpClass(cls):
        """Set up unittest check"""
        cls.new_user = User()
        cls.new_user.email = "Gavi@barca.com"
        cls.new_user.password = "laces"
        cls.new_user.first_name = "Mel"
        cls.new_user.last_name = "Gibson"

    @classmethod
    def teardown(cls):
        """Tear down test check"""
        del cls.new_user
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_User_dbtable(self):
        """Test check for tablename correctness"""
        self.assertEqual(self.new_user.__tablename__, "users")

    def test_User_inheritance(self):
        """Test check for inheritance from BaseModel"""
        self.assertIsInstance(self.new_user, BaseModel)

    def test_User_attributes(self):
        """Test check for attributes"""
        self.assertTrue('email' in self.new_user.__dir__())
        self.assertTrue('first_name' in self.new_user.__dir__())
        self.assertTrue('last_name' in self.new_user.__dir__())
        self.assertTrue('password' in self.new_user.__dir__())

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_email(self):
        """Test check for email name"""
        name = getattr(self.new_user, "email")
        self.assertIsInstance(name, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_first_name(self):
        """Test check for type first_name"""
        name = getattr(self.new_user, "first_name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_last_name(self):
        """Test check for type last_name"""
        name = getattr(self.new_user, "last_name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_password(self):
        """Test check for type password"""
        name = getattr(self.new_user, "password")
        self.assertIsInstance(name, str)
