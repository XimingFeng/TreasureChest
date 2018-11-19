from django import forms

class RegisterComputer(forms.Form):
    computer_name = forms.CharField(label="Computer Name", max_length=20)

