""" Imports """
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from core.auth.serializers.register import RegisterSerializer


""" Register view set """
class RegisterViewSet(ViewSet):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    
    # Rewriting create method to add access and refresh tokens in the body of the response
    def create(self, request, *args, **kwargs):
        
        print("Enter create of register viewset")
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user) # directly generate the token with simplejwt
        
        res = {
            "refresh":str(refresh),
            "access":str(refresh.access_token),
        }
        
        return Response({
            "user": serializer.data,
            "refresh": res["refresh"],
            "token": res["access"]
        }, status=status.HTTP_201_CREATED)
        
        
