""" 
    Imports
"""
import pytest
from rest_framework.test import APIClient


""" 
    Client pytest fixture to call it from the tests
"""
@pytest.fixture
def client():
    return APIClient()






