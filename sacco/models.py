from django.db import models
from django.contrib.auth.models import User 
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.utils import timezone
import uuid
from psutil import users
from django.conf import settings
from django.urls import reverse
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


class Individual(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    purpose=models.CharField(max_length=15,choices=PURPOSE,default='Other')
    deposit_amt = models.IntegerField(_('Amt in Ksh'))
    duration_in_months=models.CharField(choices=MONTHS,default='1')
    deposited_on=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.PROTECT,primary_key=True,default=False)
    #user=models.ForeignKey(User,on_delete=models.CASCADE,default=False)
    
    def get_absolute_url(self):
        return reverse('individual-detail',args=[str(self.id)])
    def __str__(self):
        return '%s,%s'%(self.last_name,self.first_name)
    
    


class Joint(models.Model):
    partner_first_name=models.CharField(_('partner first name'),max_length=255)
    partner_last_name=models.CharField(('partner last name'),max_length=255)
    joint_amt=models.IntegerField(_('Joint depo in Ksh'),blank=True ,default=False)
    purpose=models.CharField(max_length=15,choices=PURPOSE,default='Other')
    duration_in_months=models.CharField(choices=MONTHS,default='1')
    deposited_on=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=False)
    individual=models.ForeignKey(Individual,on_delete=models.CASCADE,default=False)