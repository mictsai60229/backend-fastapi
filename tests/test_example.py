from fastapi import FastAPI
from fastapi.testclient import TestClient
import unittest

from main import app

CLIENT = TestClient(app)

class MainTestCase(unittest.TestCase):
    
    def test_hello(self):
        response = CLIENT.get("/")
        assert response.status_code == 200
        self.assertIn("app_name", response.json())

