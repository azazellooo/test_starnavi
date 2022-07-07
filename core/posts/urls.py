from django.urls import path

from .views import PostCreateAPIView, PostLikesAPIView

app_name = 'posts'
urlpatterns = [
    path('posts/', PostCreateAPIView.as_view(), name='post_create'),
    path('posts/like/<int:pk>/', PostLikesAPIView.as_view(), name='post_like')
]
