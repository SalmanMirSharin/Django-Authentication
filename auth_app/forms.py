from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm


class RegisterForm(UserCreationForm):
       
    password1 = forms.CharField(label=("Password"),widget=forms.PasswordInput(attrs={
        'class':'form-control mb-3'
    }))
    password2 = forms.CharField(label=("Password confirmation"),widget=forms.PasswordInput(attrs={
        'class':'form-control mb-3'
    }))
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
          
        widgets ={
            'username': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'first_name': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'last_name': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'email': forms.TextInput(attrs={'class':'form-control mb-3'}),
      
    }



class AuthenticationForm(AuthenticationForm):
        username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control mb-3'
    }))
        password = forms.CharField(label=("Password"),widget=forms.PasswordInput(attrs={
        'class':'form-control mb-3'
    }))
        
class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control mb-3'
    }))
    new_password1 = forms.CharField(label=('New password'), widget=forms.PasswordInput(attrs={
        'class':'form-control mb-3'
    }))
    new_password2 = forms.CharField(label=('New password confirmation'),widget=forms.PasswordInput(attrs={
        'class':'form-control mb-3'
    }))