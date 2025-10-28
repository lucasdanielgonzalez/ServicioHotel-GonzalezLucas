from django import forms
from.models import Habitacion


class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ['numero','tipo','max_huespedes','precio_noche','disponible']
        widgets={
             'numero': forms.TextInput(attrs={'class': 'form-control'}),
             'tipo': forms.Select(attrs={'class': 'form-control'}),
             'max_huespedes': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
             'precio_noche': forms.NumberInput(attrs={'class': 'form-control'}),
             'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      }
        