from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import Individual,JointLeader,CustomUser,Supervisor

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUser
    list_display=(
        "email",
        "first_name",
        "last_name",
        "date_joined",
        "last_login",
        "is_staff",
        "is_active",
        "is_superuser",
        #"is_individual",
        #"is_jointleader"
        #"is_visitor"
        "role",
    )
    list_filter=(
        "email",
        "is_staff",
        "is_active",
    )
    
    fieldsets=(
        (None,{"fields":("email","password","groups")}),
        ("Permissoins",{"fields":("is_staff","is_active")}),
    )
    add_fieldsets=(
        (None,
         {
             "classes":("wide",),
             "fields":("email","password1","password2","is_staff","is_active"),
         },
         ),
    )
    search_fields=("email",)
    ordering=("email",)



class IndividualAdmin(admin.ModelAdmin):
    list_display = ('purpose','deposit_amt', 'deposited_on','duration_in_months','user')
    list_filter = ['user']
    search_fields = ['purpose']
    #date_hierarchy = 'timestamp'

class JointLeaderAdmin(admin.ModelAdmin):
    list_display=('partner_first_name','partner_last_name','joint_amt','deposited_on','duration_in_months','user')
    list_filter=['joint_amt']
    search_fields=['partner_first_name']

class SupervisorAdmin(admin.ModelAdmin):
    list_display=('user','phone_number')
    list_filter=['phone_number']
    search_fields=['user']



admin.site.register(Individual,IndividualAdmin)
admin.site.register(JointLeader,JointLeaderAdmin)
admin.site.register(Supervisor,SupervisorAdmin)
admin.site.register(CustomUser,CustomUserAdmin)

admin.site.site_url = "/api/"