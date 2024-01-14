#!/usr/bin/python3
''' Tests for the file storage class '''

import unittest
import os
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    ''' Tests of the file storage class '''

    @classmethod
    def setUp(self):
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = 'file.json'

    def setUpClass(self):
        self.my_model = BaseModel()

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        bm = BaseModel()
        models.storage.new(bm)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())

    def test_save(self):
        bm = BaseModel()
        models.storage.new(bm)
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)

    def test_reload(self):
        bm = BaseModel()
        models.storage.new(bm)
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
