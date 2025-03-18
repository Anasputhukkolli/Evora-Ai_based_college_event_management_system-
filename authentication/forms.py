from django import forms
from .models import Club

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'description', 'club_pic', 'no_of_members', 'created_by', 'contact_email', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Club Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Club Description'}),
            'no_of_members': forms.NumberInput(attrs={'class': 'form-control'}),
            'created_by': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Founder Name'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Contact Email'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
