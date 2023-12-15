""" --- Imports --- """
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from core.abstract.viewsets import AbstractViewSet
from core.post.models import Post
from core.post.serializers import PostSerializer
from core.auth.permissions import UserPermissions


""" --- Post viewset --- """
class PostViewSet(AbstractViewSet):
    http_method_names = ('post', 'get', 'put', 'delete')
    permission_classes = (UserPermissions,)
    serializer_class = PostSerializer
    
    def get_queryset(self):                        
        return Post.objects.all()
    
    
    def get_object(self):                
        obj = Post.objects.get_object_by_public_id(self.kwargs['pk'])                        
        self.check_object_permissions(self.request, obj)        
        return obj
    
    
    def create(self, request, *args, **kwargs):                
        # get_serializer returns a serializer instance
        serializer = self.get_serializer(data=request.data)        
        serializer.is_valid(raise_exception=True)
        
        # perform_create method creates a post object through a serializer
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    # @action creates a new route for this resource api/post/post_pk/like/
    # detail=True allows passing the ID to the URL request
    @action(methods=['post'], detail=True)
    def like(self, request, *args, **kwargs):                
        post = self.get_object() # by the id passed in the url        
        user = self.request.user # to call like method added to the User model                                
        user.like(post)        
        serializer = self.serializer_class(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(methods=['post'], detail=True)
    def remove_like(self, request, *args, **kwargs):
        post = self.get_object()
        user = self.request.user
        user.remove_like(post)
        serializer = self.serializer_class(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    

