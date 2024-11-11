#from django.contrib.auth.models import User 
#from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.utils import timezone
import uuid
from psutil import users
from django.conf import settings
from django.urls import reverse

import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from rest_framework.authtoken.models import Token
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

PURPOSE=(
    ("Business","Business"),
    ("Education","Education"),
    ("Health","Health"),
    ("Other","Other")
)


#class Month(models.TextChoices):
MONTHS=(
   ("1","1"),
   ("2","2"),
   ("3","3"),
   ("4","4"),
   ("5","5"),
   ("6","6"),
   ("7","7"),
   ("8","8"),
   ("9","9"),
   ("10","10"),
   ("11","11"),
   ("12","12"),

)

ROLE_CHOICES=[
        ('individual','individual'),
        ('joint leader','joint Leader'),
        ('supervisor','supervisor'),
]



class CustomUser(AbstractUser):
    role=models.CharField(max_length=15,choices=ROLE_CHOICES)
    username = None
    user_id=models.UUIDField(default=uuid.uuid4,editable=False)
    email = models.EmailField(_('email address'), unique=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    #is_admin=models.BooleanField(default=False)
    #is_individual=models.BooleanField(default=False)
    #is_jointleader=models.BooleanField(default=False)
    #is_visitor=models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name='customuser'
        verbose_name_plural='customusers'

    '''def get_username(self):
      return self.email'''

    


class Individual(models.Model):
    
    purpose=models.CharField(max_length=15,choices=PURPOSE,default='Other')
    deposit_amt = models.IntegerField(_('Amt in Ksh'))
    duration_in_months=models.CharField(choices=MONTHS,default='1',max_length=2)
    deposited_on=models.DateTimeField(auto_now_add=True)
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,primary_key=True,default=False)
    #user=models.ForeignKey(User,on_delete=models.CASCADE,default=False)
    
    '''def get_absolute_url(self):
        return reverse('individual-detail',args=[str(self.id)])'''
    
    def __str__(self):
        return self.user.first_name
    


class JointLeader(models.Model):
    partner_first_name=models.CharField(_('partner first name'),max_length=255)
    partner_last_name=models.CharField(('partner last name'),max_length=255)
    joint_amt=models.IntegerField(_('Joint depo in Ksh'),blank=True ,default=False)
    purpose=models.CharField(max_length=15,choices=PURPOSE,default='Other')
    duration_in_months=models.CharField(choices=MONTHS,default='1',max_length=2)
    deposited_on=models.DateTimeField(auto_now_add=True)
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,primary_key=True,default=False)
    #individual=models.ForeignKey(Individual,on_delete=models.CASCADE,default=False)
    
    '''def __str__(self):
        return self.user.JointLeader.partner_first_name'''
    
class Supervisor(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,primary_key=True,default=False)
    phone_number=PhoneNumberField(blank=True)