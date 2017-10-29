from django import forms

MESS_CHOICES = [
    (0,'---Select Mess Block---'),
    (1, 'Mess Block 1'),
    (2, 'Mess Block 2'),
    (3, 'Mess Block 3'),
    (4, 'Mess Block 4'),
    (5, 'Mess Block 5'),
]

DAYS = [
    ('zero','---Select Weekday---'),
    ('monday','Monday'),
    ('tuesday','Tuesday'),
    ('wednesday','Wednesday'),
    ('thursday','Thursday'),
    ('friday','Friday'),
    ('saturday','Saturday'),
    ('sunday','Sunday'),
]

class messform(forms.Form):
    messblock = forms.CharField(label='',widget=forms.Select(choices=MESS_CHOICES,attrs={'class':'messform'}))
    days = forms.CharField(label='',widget=forms.Select(choices=DAYS,attrs={'class':'messform'}))