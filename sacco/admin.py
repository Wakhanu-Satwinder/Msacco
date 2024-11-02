from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import Individual,Joint,CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUser
    list_display=(
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
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
    list_display = ('purpose','deposit_amt', 'deposited_on','duration_in_months', 'user')
    list_filter = ['user']
    search_fields = ['purpose']
    #date_hierarchy = 'timestamp'

class JointAdmin(admin.ModelAdmin):
    list_display=('partner_first_name','partner_last_name','joint_amt','deposited_on','duration_in_months','individual','user')
    list_filter=['joint_amt']
    search_fields=['partner_first_name']

admin.site.register(Individual,IndividualAdmin)
admin.site.register(Joint,JointAdmin)
admin.site.register(CustomUser,CustomUserAdmin)

admin.site.site_url = "/api/"