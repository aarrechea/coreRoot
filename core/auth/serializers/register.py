""" Imports """
from rest_framework import serializers
from core.user.serializers import UserSerializer
from core.user.models import User


""" Registration serializer for requests and user creation """
class RegisterSerializer(UserSerializer):
    # Make sure the password is at least 8 characters long, and no longer than 128
    # and can't be read by the user
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ['id', 'bio', 'avatar', 'email', 'username', 'first_name', 'last_name', 'password']
        
    # Use the create_user method we wrote earlier for the UserManager to create a new user    
    def create(self, validated_data):        
        return User.objects.create_user(**validated_data)
    
