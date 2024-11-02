import datetime
from typing import Self
from urllib import request
from django.db import IntegrityError
from django.http import Http404
from django.shortcuts import get_object_or_404, render
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from psutil import STATUS_IDLE
from rest_framework import viewsets,permissions
from.serializers import UserSerializer,IndividualSerializer,JointSerializer
from . import models
from .models import CustomUser, Individual,Joint
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import action,api_view,permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
#from .permissions import IsStaffOrTargetUser
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.mixins import RetrieveModelMixin,ListModelMixin,CreateModelMixin
from rest_framework import generics
from rest_framework.generics import GenericAPIView,RetrieveAPIView
from rest_framework import status
from django.http import HttpResponseRedirect

#User=get_user_model()

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    model=CustomUser
    serializer_class=UserSerializer
    #queryset=models.User.objects.all()
    queryset=models.CustomUser.objects.all()
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes=[IsAuthenticated]

    
class ProfileView(APIView):
    model=CustomUser
    serializer_class=UserSerializer
    queryset=CustomUser.objects.all()
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request,format=None):
        content={
             'user':str(request.user),
             'email':str(request.user.email),
             #'first_name':str(request.user.first_name),
             'is_staff':str(request.user.is_staff),
             'auth':str(request.auth),
        }
        return Response(content)
    
    
class IndividualViewSet(viewsets.ModelViewSet):
    queryset=models.Individual.objects.all()
    serializer_class=IndividualSerializer
    #authentication_classes=[TokenAuthentication]
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_class=[permissions.IsAuthenticated]
    

class  IndividualDetail(generics.GenericAPIView):
    queryset=models.Individual.objects.all()
    serializer_class=IndividualSerializer
    permission_class=[permissions.IsAuthenticated]
    authentication_classes=[SessionAuthentication,BasicAuthentication]

    def get_object(self,pk):
        try:
            return Individual.objects.get(pk=pk)
        except Individual.DoesNotExist:
            raise Http404 
        
    def get(self,request,pk,format=None):
        individual=self.get_object(pk)
        serializer=IndividualSerializer(individual)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        individual=self.get_object(pk)
        serializer=IndividualSerializer(individual,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        individual=self.get_object(pk)
        individual.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JointViewSet(viewsets.ModelViewSet):
    queryset=models.Joint.objects.all()
    serializer_class=JointSerializer
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_class=[IsAuthenticated]  
     

    

         
