from django import forms
from .models import student_details


class studentlogin(forms.Form):
    us = forms.CharField(label="",
                          widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Registration No.'}))
    pw = forms.CharField(label='',
                          widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
