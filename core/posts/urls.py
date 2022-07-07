from django.urls import path

from .views import PostCreateAPIView, PostLikesAPIView, PostLikeAnalyticsAPIView

app_name = 'posts'
urlpatterns = [
    path('posts/', PostCreateAPIView.as_view(), name='post_create'),
    path('posts/like/<int:pk>/', PostLikesAPIView.as_view(), name='post_like'),
    path('posts/analytics/', PostLikeAnalyticsAPIView.as_view(), name='post_analytics')
]
