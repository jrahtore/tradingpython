from django import forms


from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import CustomUser

from django.contrib.auth.forms import UserCreationForm




class CustomUserCreationForm(UserCreationForm):
    class Meta():
        model = CustomUser
        # fields = "__all__"
        fields = ['username', 'password1', 'email',
                  'first_name', 'last_name', 'password2']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = "__all__"
