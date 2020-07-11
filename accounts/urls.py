from django.urls import path
from .views import UserSignUpView, user_login, user_logout

app_name = 'accounts'

urlpatterns = [
    path('register/', UserSignUpView.as_view(), name='usersignup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
