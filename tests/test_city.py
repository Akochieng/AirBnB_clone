#!/usr/bin/python3
from models.city import City
from unittest import TestCase

class TestCity(TestCase):
    def setUp(self):
        self.a = City()
        self.b = City()

    def tearDown(self):
        del self.a
        del self.b

    def test_init(self):
        self.assertTrue(hasattr(self.a, "name"))
        self.assertTrue(hasattr(self.b, "name"))
        self.assertTrue(hasattr(self.a, "state_id"))
        self.assertTrue(hasattr(self.b, "state_id"))

    def test_val(self):
        self.a.name = "Nairobi"
        self.b.name = "Daresalaam"
        self.assertEqual(self.a.name, "Nairobi")
        self.assertEqual(self.b.name, "Daresalaam")
