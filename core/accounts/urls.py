from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, UserActivityAPIView

app_name = 'accounts'
urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    path('users/activity/<int:pk>/', UserActivityAPIView.as_view())
]
