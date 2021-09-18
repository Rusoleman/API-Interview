from django import forms


class NameForm(forms.Form):
    input_name = forms.CharField()
    input_age = forms.IntegerField()
    happy_check = forms.BooleanField()
    healthy_check = forms.BooleanField()
    busy_check = forms.BooleanField()