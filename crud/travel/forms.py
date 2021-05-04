from django import forms
from .models import Passenger

class Itemforms(forms.ModelForm):
    class Meta:
        model=Passenger
        fields="__all__"

