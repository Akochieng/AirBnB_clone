#!/usr/bin/python3
from models.review import Review
from unittest import TestCase

class TestReview(TestCase):
    def setUp(self):
        self.a = Review()
        self.b = Review()

    def tearDown(self):
        del self.a
        del self.b

    def test_init(self):
        self.assertTrue(hasattr(self.a, "text"))
        self.assertTrue(hasattr(self.b, "text"))
        self.assertTrue(hasattr(self.a, "place_id"))
        self.assertTrue(hasattr(self.a, "place_id"))
        self.assertTrue(hasattr(self.b, "user_id"))
        self.assertTrue(hasattr(self.b, "user_id"))

    def test_val(self):
        self.a.place_id = "Hospital"
        self.b.user_id = "Swimming Pool"
        self.assertEqual(self.a.place_id, "Hospital")
        self.assertEqual(self.b.user_id, "Swimming Pool")
