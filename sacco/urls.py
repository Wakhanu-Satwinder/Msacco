from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView,LogoutView,UserDetailsView
from sacco.views import IndividualDetail
from sacco import views
from allauth.account.views import confirm_email

#from django.conf.urls import url

app_name='sacco'
urlpatterns=[
    path('register/',RegisterView.as_view(),name="rest_register"),
    path('login/',LoginView.as_view(),name="rest_login"),
    path('logout/',LogoutView.as_view(),name="rest_logout"),
    path('user/',UserDetailsView.as_view(),name="rest_user_details"),
    path('profile/',views.ProfileView.as_view(),name="profile"),
    path("Idetail/<int:pk>/",IndividualDetail.as_view(),name="individual_detail"),
   
]
