from django import forms
from messmenu.models import menu

class adminlogin(forms.Form):
    aid = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Admin ID'}))
    pw = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))

DAYS = [
    ('zero','---Select Weekday---'),
    ('Monday','Monday'),
    ('Tuesday','Tuesday'),
    ('Wednesday','Wednesday'),
    ('Thursday','Thursday'),
    ('Friday','Friday'),
    ('Saturday','Saturday'),
    ('Sunday','Sunday'),
]

TYPE = [
    ('zero','---Select Meal Type---'),
    ('Breakfast','Breakfast'),
    ('Lunch','Lunch'),
    ('Dinner','Dinner'),
]



class enterdetails(forms.Form):
    days = forms.CharField(label='', widget=forms.Select(choices=DAYS, attrs={'class': 'messform'}))
    tp=forms.CharField(label='', widget=forms.Select(choices=TYPE, attrs={'placeholder':'Enter Meal Type','class':'field1'}))
    fd=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Enter Meal Details','class':'field2'}))

    """class Meta:
        model=menu
        fields = ('tp','fd')
    """