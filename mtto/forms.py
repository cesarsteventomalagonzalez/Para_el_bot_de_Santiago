from django import forms
from .models import Cargo



class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['descripcion','estado']
        widgets = {
            'descripcion' :forms.TextInput(attrs={
                'placeholder':'ingrese cargo',
                'class': 'form-gropup',
                'required':True,
            }),
        }

