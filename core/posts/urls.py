from django.urls import path

from .views import PostCreateAPIView

app_name = 'posts'
urlpatterns = [
    path('posts/', PostCreateAPIView.as_view(), name='post_create'),
]
