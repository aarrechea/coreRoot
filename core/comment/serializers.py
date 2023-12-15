""" 
    Imports 
"""
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from core.abstract.serializers import AbstractSerializer
from core.user.models import User
from core.user.serializers import UserSerializer
from core.comment.models import Comment
from core.post.models import Post


""" 
    Comment serializer
"""
class CommentSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')
    post = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='public_id')
    
    # to modify the final object by adding information about the author.
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep['author'])
        rep['author'] = UserSerializer(author).data        
        return rep
    
    
    def validate_post(self, value):
        if self.instance:
            return self.instance.post # return the post in the comment instance
        return value
        
    
    def update(self, instance, validated_data):
        print(f"Instance: {instance} - Instance edited: {instance.edited}")
        
        if not instance.edited:
            validated_data['edited'] = True
            
        instance = super().update(instance, validated_data)
        return instance
    
    
    class Meta:
        model = Comment
        
        # List of all fields that can be included in a request or a response
        fields = ['id', 'post', 'author', 'body', 'edited', 'created', 'updated']
        read_only_fields = ['edited']


