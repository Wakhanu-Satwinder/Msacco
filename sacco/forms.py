from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=CustomUser
        #fields=("email","groups")
        fields=("email","groups")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=("email","groups")
        