from urllib.request import Request
from rest_framework import serializers
from .models import Individual,JointLeader,Supervisor
from sacco.models import CustomUser,ROLE_CHOICES
from django.conf import settings
from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction


class CustomRegisterSerializer(RegisterSerializer):
    role=serializers.ChoiceField(choices=ROLE_CHOICES)
    first_name=serializers.CharField(max_length=15)
    last_name=serializers.CharField(max_length=15)

    class Meta:
        model=CustomUser
        fields=('email','first_name','last_name','password1','password2','role')        
    def get_cleaned_data(self):
        return{
            #'username':self.validated_data.get('username',''),
            'password1':self.validated_data.get('password1',''),
            'password2':self.validated_data.get('password2',''),
            'email':self.validated_data.get('email',''),
            'first_name':self.validated_data.get('first_name',''),
            'last_name':self.validated_data.get('last_name',''),
            'role':self.validated_data.get('role'),

        }
    
    @transaction.atomic
    def save(self,request):
        adapter=get_adapter()
        user=adapter.new_user(request)
        self.cleaned_data=self.get_cleaned_data()
        user.role=self.cleaned_data.get('role')
        user.first_name=self.cleaned_data.get('first_name')
        user.last_name=self.cleaned_data.get('last_name')
        #user.username=self.cleaned_data.get('username')
        user.email=self.cleaned_data.get('email') 

        user.save()
        adapter.save_user(request,user,self)
        return user
    

#STILL IN PROGRES...

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['url','user_id','email','first_name','last_name','role']
        #extra_kwargs={'password':{'write_only':True}}


class IndividualSerializer(serializers.HyperlinkedModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Individual
        fields=['url','purpose','deposit_amt','duration_in_months','deposited_on','user']

class JointLeaderSerializer(serializers.HyperlinkedModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=JointLeader
        fields=['url','partner_first_name','partner_last_name','joint_amt','duration_in_months','deposited_on','user'] 
        
class SupervisorSerializer(serializers.HyperlinkedModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Supervisor
        fields=('url','user','phone_number')