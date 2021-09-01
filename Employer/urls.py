from django.urls import path
from Employer import views

urlpatterns=[
    path("accounts/register",views.UserSignUpView.as_view(),name="signup"),
    # path("home",views.UserSignUpView.as_view(),name="home"),
    path("accounts/login",views.UserSignInView.as_view(),name="signin"),
]