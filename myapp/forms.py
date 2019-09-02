from .models import Pet
from django import forms


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ['available']
