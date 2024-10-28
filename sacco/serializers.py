from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Individual,Joint

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('url','id','username','email','is_staff')
        #fields=('id','username','email','is_staff')
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
        #lookup_field='username'               

