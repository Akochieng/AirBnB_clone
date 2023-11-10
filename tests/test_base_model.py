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
        self.assertIsInstance(self.baseone.id, str)
        self.assertEqual(len(self.baseone.id), 36)
        self.assertIsInstance(self.baseone.created_at, datetime)
        self.assertIsInstance(self.baseone.updated_at, datetime)
        self.assertIsInstance(self.basetwo.id, str)
        self.assertEqual(len(self.basetwo.id), 36)
        self.assertIsInstance(self.basetwo.created_at, datetime)
        self.assertIsInstance(self.basetwo.updated_at, datetime)

    def test_save(self):
        self.baseone.save()
        self.assertNotEqual(self.baseone.updated_at, self.baseone.created_at)
