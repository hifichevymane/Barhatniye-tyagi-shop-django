from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import CustomUser
from django import forms
from phonenumber_field.formfields import PhoneNumberField


# Registration form
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput({'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput({'class': 'form-control'}))
    email = forms.CharField(label='Электроная почта', widget=forms.EmailInput({'class': 'form-control'}))
    phone_number = PhoneNumberField(label='Номер телефона', widget=forms.EmailInput({'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput({'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput({'class': 'form-control'}))
    
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2')


# Login form
class LoginForm(forms.Form):
    email = forms.CharField(label='Электроная почта', widget=forms.EmailInput({'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput({'class': 'form-control'}))
