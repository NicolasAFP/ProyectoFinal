from django import forms
from .models import Opinion

class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ['contenido']  

class Curso_formulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()