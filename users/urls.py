# users/urls.py
from django.urls import path
from .views import UserCreateView, ObtainTokenView

urlpatterns = [
    path('users/register/', UserCreateView.as_view(), name='user-create'),
    path('token/', ObtainTokenView.as_view(), name='token-create'),

    # Add other URLs as needed
]
