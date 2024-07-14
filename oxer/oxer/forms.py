from django import forms

class usersForm(forms.Form):
    fname = forms.CharField(label="First Name")
    lname = forms.CharField(label="Last Name")