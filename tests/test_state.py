#!/usr/bin/python3
from models.state import State
from unittest import TestCase

class TestState(TestCase):
    def setUp(self):
        self.statea = State()
        self.stateb = State()

    def tearDown(self):
        del self.statea
        del self.stateb

    def test_init(self):
        self.assertTrue(hasattr(self.statea, "name"))
        self.assertTrue(hasattr(self.stateb, "name"))

    def test_val(self):
        self.statea.name = "Kenya"
        self.stateb.name = "Tanzania"
        self.assertEqual(self.statea.name, "Kenya")
        self.assertEqual(self.stateb.name, "Tanzania")
