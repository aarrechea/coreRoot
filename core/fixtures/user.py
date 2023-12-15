""" 
    Imports
"""
import pytest
from core.user.models import User


""" 
    Data user
"""
data_user = {
    'username':'test_user',
    'email':'test@gmail.com',
    'first_name':'Test',
    'last_name':'User',
    'password':'test_password'
}

# it labels the function as a fixture. We can now import the user function in any test
# and pass it as an argument to the test function
@pytest.fixture 
def user(db)->User:
    return User.objects.create_user(**data_user)




