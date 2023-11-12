#!/usr/bin/python3
from unittest import TestCase
from models.place import Place


class TestPlace(TestCase):
    def setUp(self):
        self.a = Place()
        self.b = Place()

    def tearDown(self):
        del self.a
        del self.b

    def test_init(self):
        self.assertTrue(hasattr(self.a, "city_id"))
        self.assertTrue(hasattr(self.b, "city_id"))
        self.assertTrue(hasattr(self.a, "user_id"))
        self.assertTrue(hasattr(self.b, "user_id"))
        self.assertTrue(hasattr(self.a, "name"))
        self.assertTrue(hasattr(self.b, "name"))
        self.assertTrue(hasattr(self.a, "description"))
        self.assertTrue(hasattr(self.b, "description"))
        self.assertTrue(hasattr(self.a, "number_rooms"))
        self.assertTrue(hasattr(self.b, "number_rooms"))
        self.assertTrue(hasattr(self.a, "number_bathrooms"))
        self.assertTrue(hasattr(self.b, "number_bathrooms"))
        self.assertTrue(hasattr(self.a, "max_guest"))
        self.assertTrue(hasattr(self.b, "max_guest"))
        self.assertTrue(hasattr(self.a, "price_by_night"))
        self.assertTrue(hasattr(self.b, "price_by_night"))
        self.assertTrue(hasattr(self.a, "latitude"))
        self.assertTrue(hasattr(self.b, "latitude"))
        self.assertTrue(hasattr(self.a, "longitude"))
        self.assertTrue(hasattr(self.b, "longitude"))

    def test_val(self):
        self.assertEqual(self.a.city_id, "")
        self.assertEqual(self.b.city_id, "")
        self.assertEqual(self.a.user_id, "")
        self.assertEqual(self.b.user_id, "")
        self.assertEqual(self.a.name, "")
        self.assertEqual(self.b.name, "")
        self.assertEqual(self.a.description, "")
        self.assertEqual(self.b.description, "")
        self.assertEqual(self.a.number_bathrooms, 0)
        self.assertEqual(self.b.number_bathrooms, 0)
        self.assertEqual(self.a.number_rooms, 0)
        self.assertEqual(self.b.number_rooms, 0)
        self.assertEqual(self.a.max_guest, 0)
        self.assertEqual(self.b.max_guest, 0)
        self.assertEqual(self.a.price_by_night, 0)
        self.assertEqual(self.b.price_by_night, 0)
        self.assertEqual(self.a.latitude, 0.0)
        self.assertEqual(self.b.latitude, 0.0)
        self.assertEqual(self.a.longitude, 0.0)
        self.assertEqual(self.b.longitude, 0.0)
