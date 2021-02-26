from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from . import forms

urlpatterns = [
    path('login/',LoginView.as_view(template_name='accounts/login.html',form_class=forms.LoginForm), name="login"),
    path('profile/',views.profile, name="profile"),
    path('profile/edit',views.profile_edit, name="profile_edit"),
    path('signup/',views.signup, name="signup"),
    path('logout/',LogoutView.as_view(), name="logout"),
]
