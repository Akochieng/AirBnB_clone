#!/usr/bin/python3
from models.base_model import BaseModel
from unittest import TestCase
from unittest.mock import Mock
from datetime import datetime
import re

class TestBase(TestCase):
    def setUp(self):
        self.mockedBase = Mock(spec=BaseModel)
        self.eyed = "ad8bb9c6-ff2b-4884-bd86-68e854b18fac"
        time = datetime(2023, 11, 10, 12, 21, 22, 246397)
        self.updatetime = datetime(2024, 1, 10, 12, 21, 22, 246397)
        self.mockedBase.return_value = BaseModel(id=self.eyed,created_at=time, updated_at=time)
        self.baseone = self.mockedBase()

    def tearDown(self):
        del self.baseone

    def test_init(self):
        self.assertEqual(self.baseone.id, self.eyed)
        self.assertIsInstance(self.baseone.created_at, datetime)
        self.assertIsInstance(self.baseone.updated_at, datetime)

    def test_save(self):
        self.baseone.save()
        self.assertNotEqual(self.baseone.updated_at, self.baseone.created_at)
