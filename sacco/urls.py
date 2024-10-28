from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView,LogoutView,UserDetailsView
from .views import IndividualDetail 
from sacco import views


app_name='sacco'
urlpatterns=[
    path('register/',RegisterView.as_view(),name="rest_register"),
    path('login/',LoginView.as_view(),name="rest_login"),
    path('logout/',LogoutView.as_view(),name="rest_logout"),
    path('user/',UserDetailsView.as_view(),name="rest_user_details"),
    path('profile/',views.ProfileView.as_view(),name="profile"),
    path("Idetail/<int:pk>/",IndividualDetail.as_view(),name="individual_detail"),
    path(r'^individuall/$',views.IndividualViewSet.as_view({'get:list'}),name='individual-list')
    #path('hello//',views.hello_world,name='hello_world'),
   
]  
