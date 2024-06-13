from django import forms 
from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'document_id', 'event', 'status']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
            'phone_number': 'Número de teléfono',
            'document_id': 'Documento',
            'event': 'Evento',
            'status': 'Estado',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Apellido', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Número de teléfono', 'class': 'form-control'}),
            'document_id': forms.TextInput(attrs={'placeholder': 'Documento', 'class': 'form-control'}),
            'event': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
