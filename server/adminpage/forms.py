from django import forms

class adminlogin(forms.Form):
    aid = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Admin ID'}))
    pw = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))