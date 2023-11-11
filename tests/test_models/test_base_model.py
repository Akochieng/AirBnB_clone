#!/usr/bin/python3
from models.base_model import BaseModel
from unittest import TestCase
from unittest.mock import Mock
from datetime import datetime
import re

class TestBase(TestCase):
    def setUp(self):
        self.baseone = BaseModel()
        self.basetwo = BaseModel()

    def tearDown(self):
        del self.baseone
        del self.basetwo

    def test_init(self):
        self.assertTrue(hasattr(self.baseone, "id"))
        self.assertTrue(hasattr(self.baseone, "created_at"))
        self.assertTrue(hasattr(self.baseone, "updated_at"))
        self.assertTrue(hasattr(self.basetwo, "id"))
        self.assertTrue(hasattr(self.basetwo, "created_at"))
        self.assertTrue(hasattr(self.basetwo, "updated_at"))

    def test_times(self):
        self.assertIsInstance(self.baseone.created_at, datetime)
        self.assertIsInstance(self.baseone.updated_at, datetime)
        self.assertIsInstance(self.basetwo.created_at, datetime)
        self.assertIsInstance(self.basetwo.updated_at, datetime)

    def test_id(self):
        self.assertIsInstance(self.basetwo.id, str)
        self.assertIsInstance(self.baseone.id, str)
        self.assertEqual(len(self.baseone.id), 36)
        self.assertEqual(len(self.basetwo.id), 36)

    def test_save(self):
        self.baseone.save()
        self.assertNotEqual(self.baseone.updated_at, self.baseone.created_at)
