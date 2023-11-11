#!/usr/bin/python3
from models.user import User
from unittest import TestCase

class TestUser(TestCase):
    def setUp(self):
        self.usera = User()
        self.userb = User()

    def tearDown(self):
        del self.usera
        del self.userb

    def test_init(self):
        self.assertTrue(hasattr(self.usera, "first_name"))
        self.assertTrue(hasattr(self.usera, "last_name"))
        self.assertTrue(hasattr(self.usera, 'email'))
        self.assertTrue(hasattr(self.usera, "password"))

    def test_vals(self):
        self.usera.first_name = "Alphonce"
        self.usera.last_name = "Kochieng"
        self.usera.email = "adkochieng@telkom.co.ke"
        self.assertEqual(self.usera.first_name, "Alphonce")
        self.assertEqual(self.usera.last_name, "Kochieng")
        self.assertEqual(self.usera.email, "adkochieng@telkom.co.ke")
