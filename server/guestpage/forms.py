from django import forms
from .models import guestreg
MESS_CHOICES = [
    (0,'---Select Mess Block---'),
    (1, 'Mess Block 1'),
    (2, 'Mess Block 2'),
    (3, 'Mess Block 3'),
    (4, 'Mess Block 4'),
    (5, 'Mess Block 5'),
]

TYPE = [
    ('zero','---Select Meal Type---'),
    ('Breakfast','Breakfast'),
    ('Lunch','Lunch'),
    ('Dinner','Dinner'),
]



class guestform(forms.ModelForm):
    fname = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    lname = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    block = forms.CharField(label='',widget=forms.Select(choices=MESS_CHOICES,attrs={'class':'messblock'}))
    meal = forms.CharField(label='',widget=forms.Select(choices=TYPE,attrs={'class':'mealtype'}))
    date = forms.DateField(label='',widget=forms.DateInput(attrs={'class':'dt','placeholder':'Date : YYYY-MM-DD'}))

    class Meta:
        model=guestreg
        fields = ('fname','lname','block','meal','date')