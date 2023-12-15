""" 
    Imports
"""
import pytest
from core.fixtures.user import user
from core.post.models import Post


""" 
    Fixture to create a post injecting the user fixture into it
"""
@pytest.fixture
def post(db, user):
    return Post.objects.create(author=user, body='Test Post Body')



