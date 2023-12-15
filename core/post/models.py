""" --- Imports --- """
from django.db import models
from core.abstract.models import AbstractModel, AbstractManager


""" --- Post manager --- """
class PostManager(AbstractManager):
    pass


""" --- Class Post --- """
class Post(AbstractModel):
    author = models.ForeignKey(to='core_user.User', on_delete=models.CASCADE)
    body = models.TextField()
    edited = models.BooleanField(default=False)
    objects = PostManager()
    
    def __str__(self):
        return f"{self.author.name}"

    class Meta:
        db_table = "core_post"


