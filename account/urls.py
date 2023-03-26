from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('token-auth/', obtain_auth_token, name='api_token_auth'),
]