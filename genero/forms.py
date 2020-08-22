from django import forms
from genero.models import Genero


class GeneroForm(forms.Form):
    class Meta:
        model = Genero
        fields = '__all__'