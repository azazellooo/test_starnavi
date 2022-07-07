from django.urls import path

from .views import RegistrationAPIView, LoginAPIView

app_name = 'accounts'
urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
]
