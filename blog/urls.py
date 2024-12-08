from django.urls import path
from blog.views import (
    PostListAPIView,
    PostCreateAPIView,
    PostRetrieveAPIView,
    PostUpdateAPIView,
    PostDestroyAPIView,
    CommentListAPIView,
    CommentCreateAPIView,
    CommentRetrieveAPIView,
    CommentUpdateAPIView,
    CommentDestroyAPIView,
)
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    # Posts
    path("posts/", PostListAPIView.as_view(), name="post-list"),
    path("post/create/", PostCreateAPIView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostRetrieveAPIView.as_view(), name="post-retrieve"),
    path(
        "post/<int:pk>/update/", PostUpdateAPIView.as_view(), name="post-update"
    ),
    path(
        "post/<int:pk>/delete/", PostDestroyAPIView.as_view(), name="post-delete"
    ),
    # Comments
    path("comments/", CommentListAPIView.as_view(), name="comment-list"),
    path("comment/create/", CommentCreateAPIView.as_view(), name="comment-create"),
    path("comment/<int:pk>/", CommentRetrieveAPIView.as_view(), name="comment-retrieve"),
    path("comment/<int:pk>/update/", CommentUpdateAPIView.as_view(), name="comment-update"),
    path("comment/<int:pk>/delete/", CommentDestroyAPIView.as_view(), name="comment-delete"),
]