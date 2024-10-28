from django.contrib import admin
from .models import Individual,Joint
# Register your models here.

class IndividualAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'purpose','deposit_amt', 'deposited_on','duration_in_months', 'user')
    list_filter = ['user']
    search_fields = ['purpose']
    #date_hierarchy = 'timestamp'

class JointAdmin(admin.ModelAdmin):
    list_display=('partner_first_name','partner_last_name','joint_amt','deposited_on','duration_in_months','individual','user')
    list_filter=['joint_amt']
    search_fields=['partner_first_name']

admin.site.register(Individual,IndividualAdmin)
admin.site.register(Joint,JointAdmin)

admin.site.site_url = "/api/"