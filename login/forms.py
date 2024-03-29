from login.models import UserProfile
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

#class UserProfileForm(forms.ModelForm):
#    pass
#    class Meta:
#        model = UserProfile
#        fields = ('website', 'picture')