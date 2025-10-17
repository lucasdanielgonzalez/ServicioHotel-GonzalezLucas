from django import forms
from hotel.models import Huesped


class HuespedForm(forms.ModelForm):
    class Meta:
        model= Huesped
        fields=["nombre","apellido","dni","email","telefono","fecha_de_nacimiento"]
        widgets={
            "fecha_de_nacimiento":forms.DateInput(attrs={'type':'date','class':'form-control'}),
            "nombre":forms.TextInput(attrs={'class':'form-control'}),
            "apellido":forms.TextInput(attrs={'class':'form-control'}),
            "dni":forms.TextInput(attrs={'class':'form-control'}),
            "email":forms.EmailInput(attrs={'class':'form-control'}),
            "telefono": forms.TextInput(attrs={'class': 'form-control'})
        }