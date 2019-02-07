
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post', PostViewSet, basename='post')

urlpatterns = [
    path('posts/', ListPostsView.as_view(), name="posts-all"),
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/register/', RegisterUsers.as_view(), name="auth-register"),
]

urlpatterns += router.urls