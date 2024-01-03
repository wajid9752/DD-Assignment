from django import forms
from account.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'mobile', 'role', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    email = forms.CharField(validators=[validate_email])

