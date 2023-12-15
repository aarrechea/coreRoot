""" Imports """
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from core.abstract.models import AbstractManager, AbstractModel


""" User manager """
class UserManager(BaseUserManager, AbstractManager):            
    """ Create and return a user with an email, phone, username and password """
    def create_user(self, username, email, password=None, **kwargs):
        if username is None:
            raise TypeError('Users must have a username')
        if email is None:
            raise TypeError('Users mus have an email')
        if password is None:
            raise TypeError('Users mus have a password')
        
        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
        
    """ Create and return a user with superuser (admin) permissions """
    def create_superuser(self, username, email, password=None, **kwargs):
        if username is None:
            raise TypeError('Users must have a username')
        if email is None:
            raise TypeError('Users mus have an email')
        if password is None:
            raise TypeError('Users mus have a password')
        
        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True        
        user.save(using=self._db)
        
        return user
            

""" User model """
class User(AbstractModel, AbstractBaseUser, PermissionsMixin):    
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True)
    post_liked = models.ManyToManyField("core_post.Post", related_name='liked_by')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = UserManager()
    
    def __str__(self):
        return f'{self.email}'
    
    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'


    # like post if it hasn't been done yet
    def like(self, post):
        return self.post_liked.add(post)
    
    def remove_like(self, post):
        return self.post_liked.remove(post)
    
    def has_liked(self, post):
        return self.post_liked.filter(pk=post.pk).exists()
    
            

