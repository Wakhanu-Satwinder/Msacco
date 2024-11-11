from django.urls import path,include
from . import views
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView,LogoutView,UserDetailsView
from allauth.account.views import confirm_email
from .views import GenericUserAPIView,UserAPIView

app_name='sacco'
urlpatterns=[
    path('register/',RegisterView.as_view(),name="rest_register"),
    path('login/',LoginView.as_view(),name="rest_login"),
    path('logout/',LogoutView.as_view(),name="rest_logout"),
    path('user/edit/',UserDetailsView.as_view(),name="rest_user_details"),
    path('profile/',views.ProfileView.as_view(),name="profile"),
    path('user/',UserAPIView.as_view()),
    path('user/<int:id>/',GenericUserAPIView.as_view()),
]
