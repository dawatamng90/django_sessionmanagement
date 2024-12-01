from django import forms

class AddItemForm(forms.Form):
    itemname = forms.CharField()
    quantity = forms.IntegerField()
    