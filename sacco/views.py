import datetime
from typing import Self
from urllib import request
from django.db import IntegrityError
from django.http import Http404
#from django.shortcuts import get_object_or_404, render
#from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model,authenticate,login
from psutil import STATUS_IDLE
from rest_framework import viewsets,permissions
from.serializers import UserSerializer,IndividualSerializer,JointLeaderSerializer,CustomRegisterSerializer,SupervisorSerializer
from . import models
from .models import CustomUser,Individual,JointLeader
from rest_framework.response import Response
from rest_framework import permissions
#from rest_framework.decorators import action,api_view,permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.mixins import RetrieveModelMixin,ListModelMixin,CreateModelMixin
from rest_framework import generics
from rest_framework.generics import GenericAPIView,RetrieveAPIView
from rest_framework import status
#from rest_framework.authtoken.views import ObtainAuthToken
#from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .permissions import IsIndividual,IsJointLeader,IsSupervisor


#User=get_user_model()

# Create your views here.

class UserAPIView(APIView):
    @staticmethod
    def get(request):
        queryset=models.CustomUser.objects.all()
        #serializer_context={'request':request,}
        serializer=UserSerializer(queryset,many=True,context={'request':request})
        return Response(serializer.data)

class GenericUserAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,
                         mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class=UserSerializer
    queryset=CustomUser.objects.all()
    lookup_field='id'

    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.List(request)
    def post(self,request):
        return self.create(request)
    def put(self,request,id=None):
        return self.update(request,id)
    def delete(self,request,id):
        return self.destroy(request,id)



class UserViewSet(viewsets.ModelViewSet):  
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializer
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes=[IsAdminUser]

      
class ProfileView(APIView):
    serializer_class=UserSerializer
    queryset=models.CustomUser.objects.all()
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request,format=None):
        content={
             'user':str(request.user),
             'email':str(request.user.email),
             'first_name':str(request.user.first_name),
             'last_name':str(request.user.last_name),
             'is_staff':str(request.user.is_staff),
             #'auth':str(request.auth),
        }
        return Response(content)
    
    
class IndividualViewSet(viewsets.ModelViewSet):
    queryset=models.Individual.objects.all()
    serializer_class=IndividualSerializer
    #authentication_classes=[TokenAuthentication]
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes=[IsAuthenticated,IsIndividual]
    
    def perform_create(self, serializer):
        serializer.save(user=request.user)
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    


class JointViewSet(viewsets.ModelViewSet):
    queryset=models.JointLeader.objects.all()
    serializer_class=JointLeaderSerializer
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes=[IsAuthenticated,IsJointLeader]
    
    def perform_create(self, serializer):
        serializer.save(user=request.user)
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class Supervisor(viewsets.ModelViewSet):
    queryset=models.Supervisor.objects.all()
    serializer_class=SupervisorSerializer
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes=[IsAuthenticated,IsSupervisor]

    