from django.urls import path
from .views import RegisterUserView, UserRegistrationView, UserListView

urlpatterns = [
    # API Endpoints
    path('api/register/', RegisterUserView.as_view(), name='api-register'),

    # Frontend Endpoints
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user_list'),
]
