#!/usr/bin/python3
"""Test check for State"""

import unittest
from models.base_model import BaseModel
from models.state import State
from os import getenv, remove
import pep8

storage = getenv("HBNB_TYPE_STORAGE", "fs")


class TestState(unittest.TestCase):
    """Test check for State class"""
    @classmethod
    def setUpClass(cls):
        """Set up test check"""
        cls.new_state = State()
        cls.new_state.name = "California"

    @classmethod
    def tearDownClass(cls):
        """Tear down unittest check"""
        del cls.new_state
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_State_dbtable(self):
        """Test check for tablename correctness"""
        self.assertEqual(self.new_state.__tablename__, "states")

    def test_State_inheritance(self):
        """Test check for inheritance from BaseModel"""
        self.assertIsInstance(self.new_state, BaseModel)

    def test_State_attributes(self):
        """Test check for attributes"""
        self.assertTrue('name' in self.new_state.__dir__())

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_State_attributes_type(self):
        """Test check for attribute type"""
        name = getattr(self.new_state, "name")
        self.assertIsInstance(name, str)
