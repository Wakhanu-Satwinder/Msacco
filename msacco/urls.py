"""
URL configuration for msacco project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from sacco import urls as sacco_urls
from sacco import views
from rest_framework import routers
from rest_framework.routers import SimpleRouter


#from django.conf.urls import include


app_name='sacco'
#router=DefaultRouter()
router=routers.SimpleRouter()
router.register(r'users',views.UserViewSet,basename='customuser')
router.register(r'individual',views.IndividualViewSet,basename='individual')
router.register(r'jointleader',views.JointViewSet ,basename='jointleader')
router.register(r'supervisor',views.Supervisor,basename='supervisor')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('allauth.urls')),
    path('api/',include(router.urls)),
    path('apii/',include(sacco_urls)),
]