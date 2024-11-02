from urllib.request import Request
from rest_framework import serializers

from django.contrib.auth.models import Group
from .models import Individual,Joint
from sacco.models import CustomUser

#from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model
#from dj_rest_auth.serializers import UserDetailsSerializer
#from allauth.account.utils import setup_user_email

from django.conf import settings
from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    first_name=serializers.CharField(max_length=15)
    last_name=serializers.CharField(max_length=15)

    class Meta:
        model=CustomUser
        fields=('username','email','first_name','last_name','password1','password2',)
    
    def get_cleaned_data(self):
        return{
            'username':self.validated_data.get('username',''),
            'password1':self.validated_data.get('password1',''),
            'password2':self.validated_data.get('password2',''),
            'email':self.validated_data.get('email',''),
            'first_name':self.validated_data.get('first_name',''),
            'last_name':self.validated_data.get('last_name',''),

        }
    def save(self,request):
        adapter=get_adapter()
        user=adapter.new_user(request)
        self.cleaned_data=self.get_cleaned_data()
        user.first_name=self.cleaned_data.get('first_name')
        user.last_name=self.cleaned_data.get('last_name')
        user.save()
        adapter.save_user(request,user,self)
        return user
    

#STILL IN PROGRES...
'''class UserSerializer(serializers.ModelSerializer):
    groups=serializers.SlugRelatedField(many=True,read_only=True,slug_field='name')
    class Meta:
        model = CustomUser
        fields=(
            "url",
            "id",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
            "date_joined",
            "is_active",
        )
'''


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        #fields = ['url','user_id', 'email', 'first_name', 'last_name']
        fields='__all__'

class IndividualSerializer(serializers.HyperlinkedModelSerializer):
    #user=UserSerializer(read_only=True)
    class Meta:
        model=Individual
       # fields=['url','first_name','last_name','purpose','deposit_amt','duration_in_months','deposited_on','user']
        fields='__all__'
class JointSerializer(serializers.HyperlinkedModelSerializer):
    #user=UserSerializer(read_only=True)
    class Meta:
        model=Joint
        fields=['url','partner_first_name','partner_last_name','joint_amt','duration_in_months','deposited_on','individual','user'] 
                      

