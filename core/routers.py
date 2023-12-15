""" --- Imports --- """
from rest_framework_nested import routers
from core.user.viewsets import UserViewSet
from core.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet
from core.post.viewsets import PostViewSet
from core.comment.viewsets import CommentViewSet


""" --- Router --- """
router = routers.SimpleRouter()


""" --- User --- """
router.register(r'user', UserViewSet, basename='user')


""" --- Auth --- """
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')


""" --- Post --- """
router.register(r'post', PostViewSet, basename='post')

# Nested router inside post for comments. Lookup = 'post' generates that public_id with the key 'post_pk
# will be passed in the URL
posts_router = routers.NestedSimpleRouter(router, r'post', lookup='post')
posts_router.register(r'comment', CommentViewSet, basename='post-comment')


""" --- Patterns --- """
urlpatterns = [
    *router.urls,
    *posts_router.urls
]



