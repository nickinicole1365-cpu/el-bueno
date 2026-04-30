from django import forms
from django.utils import timezone
from .models import Task

class CreateNewTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'Product',
            'descripcion',
            'estado',
            'nombre',
            'fecha',
            'hora',
            'numero_telefono',
            'tipografia',
            'total',
            'anticipo'
        ]
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            ahora = timezone.localtime()
            self.fields['hora'].initial = ahora.strftime('%H:%M')
            self.fields['fecha'].initial = ahora.date()