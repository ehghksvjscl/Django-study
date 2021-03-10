from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup, name="signup"), # /accounts/signup
    path('login/',views.login, name="login"), # /accounts/login
    path('logout/',views.logout, name="logout"), # /accounts/logout
    path('edit/',views.profile_edit, name="edit"), # /accounts/edit
]
