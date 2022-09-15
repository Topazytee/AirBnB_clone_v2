#!/usr/bin/python3
"""Test check for Review"""
import unittest
from os import getenv, remove
from models.base_model import BaseModel
from models.review import Review
import pep8

storage = getenv("HBNB_TYPE_STORAGE", "fs")


class TestReview(unittest.TestCase):
    """Test check for Review class"""
    @classmethod
    def setUpClass(cls):
        """Set up unittest"""
        cls.rev = Review()
        cls.rev.user_id = "Mr and Mrs Smith 132"
        cls.rev.place_id = "Hansel and Gretel 123"
        cls.rev.text = "The strongest in the Multiverse"

    def tearDownClass(cls):
        """Tear down unittest"""
        del cls.rev
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_style_check(self):
        """Test check for pep8 Style Guide"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "pep8 error needs fixing")

    def test_Review_dbtable(self):
        """Test check for table correctness"""
        self.assertEqual(self.rev.__tablename__, "reviews")

    def test_Review_inheritance(self):
        """Test check for class inheritance from BaseModel"""
        self.assertIsInstance(self.rev, BaseModel)

    def test_Review_attributes(self):
        """Test check for attributes"""
        self.assertTrue('place_id' in self.rev.__dir__())
        self.assertTrue('user_id' in self.rev.__dir__())
        self.assertTrue('text' in self.rev.__dir__())

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_Review_attributes(self):
        """Test check for attributes"""
        place_id = getattr(self.rev, "place_id")
        user_id = getattr(self.rev, "user_id")
        text = getattr(self.rev, "text")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)
