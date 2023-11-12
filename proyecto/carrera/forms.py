from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = [
            "numero_identificacion",
            "nombres",
            "apellidos",
            "edad",
            "correo_electronico",
            "genero",
            "distancia",
            "categoria",
        ]