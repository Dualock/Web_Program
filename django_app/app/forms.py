from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Clave', max_length=100, widget=forms.PasswordInput)

class SignupForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Clave', max_length=100, widget=forms.PasswordInput)
