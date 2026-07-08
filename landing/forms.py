from django import forms
from .models import Postulante


class PostulanteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for campo in self.fields.values():
            campo.error_messages = {
                'required': 'Este campo es obligatorio ⚡',
                'invalid': 'Ingresa un dato válido ⚡'
            }

    class Meta:
        model = Postulante
        fields = [
            'nombre',
            'email',
            'edad',
            'objetivo',
            'compromiso',
            'dificultad_actual',
            'experiencia_previa',
            'motivacion',
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre completo'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}),
            'edad': forms.NumberInput(attrs={'placeholder': 'Edad'}),
            'objetivo': forms.Select(),
            'compromiso': forms.NumberInput(attrs={
                'placeholder': 'Nivel de compromiso del 1 al 10',
                'min': '1',
                'max': '10'
            }),
            'dificultad_actual': forms.Textarea(attrs={
                'placeholder': '1. ¿Cuál es tu principal dificultad hoy?'
            }),
            'experiencia_previa': forms.Textarea(attrs={
                'placeholder': '2. ¿Has seguido antes un plan nutricional o de entrenamiento?'
            }),
            'motivacion': forms.Textarea(attrs={
                'placeholder': '3. ¿Por qué quieres ingresar al Programa Strong?'
            }),
        }