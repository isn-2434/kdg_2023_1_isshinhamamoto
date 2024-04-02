from django import forms

class YourInputForm(forms.Form):
    title = forms.CharField(max_length=100)
    thumbnail = forms.ImageField()