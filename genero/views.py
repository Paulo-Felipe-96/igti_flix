from django.shortcuts import render
from . import forms

# Create your views here.


def cadastro(request):
    form = forms.GeneroForm()
    data_dict = {'form': form}
    return render(request, 'genero/genero.html', data_dict)