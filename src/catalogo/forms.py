from django.forms import ModelForm
from django import forms
from .models import (
    Usuario
)


class FormLogin(ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password']


class FormRegister(forms.ModelForm):
    nombres = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingresa tu nombre completo',
            }
        )
    )

    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingresa tu nombre de usuario',
            }
        )
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Ingresa tu Correo electronico',
            }
        )
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Ingresa tu contraseña',
            }
        )
    )
    imagen = forms.ImageField(
        label='',
        required=False)

    class Meta:
        model = Usuario
        fields = ['nombres', 'username', 'email', 'password', 'imagen']
