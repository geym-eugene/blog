from django.urls import path
from rest_framework.permissions import AllowAny

from user.apps import UserConfig

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user.views import UserCreateAPIView, UserListAPIView, UserUpdateAPIView, UserRetrieveAPIView, UserDestroyAPIView

app_name = UserConfig.name

urlpatterns = [
    path("user_list/", UserListAPIView.as_view(), name="user-list"),
    path("user_update/", UserUpdateAPIView.as_view(), name="user-update"),
    path("user_retrieve/", UserRetrieveAPIView.as_view(), name="user-retrieve"),
    path("user_delete/", UserDestroyAPIView.as_view(), name="user-delete"),
    # User registration
    path("register/", UserCreateAPIView.as_view(), name="register"),
    # JWT token
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token-refresh",
    ),
]
