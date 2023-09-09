from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=16, label='Parolni kiriting', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=16, label='Parolni qayta kiriting',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email']

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Parollar bir xil emas')
        return data['password2']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'birth_of_date']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


