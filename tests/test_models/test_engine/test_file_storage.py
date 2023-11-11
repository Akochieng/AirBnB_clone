#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from unittest import TestCase


class TestFileStorage(TestCase):
    def setUp(self):
        self.a = FileStorage()
        self.b = FileStorage()

    def tearDown(self):
        del self.a
        del self.b

    def test_init(self):
        self.assertTrue(hasattr(self.a, "_FileStorage__file_path"))
        self.assertTrue(hasattr(self.b, "_FileStorage__file_path"))
        self.assertTrue(hasattr(self.a, "_FileStorage__objects"))
        self.assertTrue(hasattr(self.b, "_FileStorage__objects"))
