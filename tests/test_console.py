#!/usr/bin/python3
"""Unittest tests for the console"""


import sys
import models
import unittest
from models import storage
from models import State
from models.engine.db_storage import DBStorage
from io import StringIO
from console import HBNBCommand
from unittest.mock import create_autospec
from os import getenv

db = getenv("HBNB_TYPE_STORAGE", "fs")


class test_console(unittest.TestCase):
    """Unittest for console module"""
    def setUp(self):
        """Test setup"""
        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def tearDown(self):
        """Test teardown"""
        sys.stdout = self.backup

    def create(self):
        """Create an instance of HBNBCommand class"""
        return HBNBCommand()

    def test_quit(self):
        """Test quit"""
        console = self.create()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF(self):
        """Test EOF"""
        console = self.create()
        self.assertTrue(console.onecmd("EOF"))

    def test_all(self):
        """Test all"""
        console = self.create()
        console.onecmd("all")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    @unittest.skipIf(db == "db", "Testing database storage only")
    def test_show(self):
        """Test show"""
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User " + user_id)
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertTrue(str is type(x))

    @unittest.skipIf(db == "db", "Testing database storage only")
    def test_show_class_name(self):
        """Test for class name"""
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show")
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** class name missing **\n", x)

    def test_show_class_name(self):
        """Test for missing id"""
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User")
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** instance id missing **\n", x)

    @unittest.skipIf(db == "db", "Testing database storage only")
    def test_show_no_instance_found(self):
        """Test for missing instance"""
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User " + "12345678")
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** no instance found **\n", x)

    def test_create(self):
        """Test create"""
        console = self.create()
        console.onecmd("create User email=ego@hbnb.com password=abc")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    def test_class_name(self):
        """Test missing class name"""
        console = self.create()
        console.onecmd("create")
        x = (self.capt_out.getvalue())
        self.assertEqual("** class name missing **\n", x)

    def test_class_name_doesnt_exist(self):
        """Test missing class name"""
        console = self.create()
        console.onecmd("create Avatar")
        x = (self.capt_out.getvalue())
        self.assertEqual("** class doesn't exist **\n", x)

    @unittest.skipIf(db != 'db', "Testing DBstorage only")
    def test_create_db(self):
        """Test for DB storage"""
        console = self.create()
        console.onecmd("create State name=California")
        result = storage.all("State")
        self.assertTrue(len(result) > 0)
