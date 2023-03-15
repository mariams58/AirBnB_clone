#!/usr/bin/python3
""" Unittest modules for the User Class """

import unittest
from models.user import User
from datetime import datetime
import os
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Test cases for User class """
    def setUp(self):
        """ Sets up the test methods """
        pass

    def tearDown(self):
        """ Tears down test Methods """
        self.resetStorage()
        pass

    def resetStorage(self):
        """ Resets FileStorage data """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)


if __name__ == "__main__":
    unittest.main()
