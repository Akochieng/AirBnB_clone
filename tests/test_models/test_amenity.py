#!/usr/bin/python3
from models.amenity import Amenity
from unittest import TestCase

class TestAmenity(TestCase):
    def setUp(self):
        self.a = Amenity()
        self.b = Amenity()

    def tearDown(self):
        del self.a
        del self.b

    def test_init(self):
        self.assertTrue(hasattr(self.a, "name"))
        self.assertTrue(hasattr(self.b, "name"))
        self.assertEqual(self.a.name, "")
        self.assertEqual(self.b.name, "")
        self.assertTrue(hasattr(self.b, "id"))
        self.assertTrue(hasattr(self.b, "created_at"))
        self.assertTrue(hasattr(self.b, "updated_at"))

    def test_val(self):
        self.a.name = "Hospital"
        self.b.name = "Swimming Pool"
        self.assertEqual(self.a.name, "Hospital")
        self.assertEqual(self.b.name, "Swimming Pool")
