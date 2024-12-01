from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=100)

class AgeForm(forms.Form):
    age = forms.IntegerField(label="Your Age", min_value=0)

class GfForm(forms.Form):
    gfname = forms.CharField(label="Girlfriend's Name", max_length=100)
