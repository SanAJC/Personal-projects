from django import forms
from .models import Asistencia

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['nombre', 'apellido', 'email', 'numero_telefonico', 'materia']
