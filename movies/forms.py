from django import forms
from .models import movies
from .models import user

class moviesForm(forms.ModelForm):
    class Meta:
        model = movies
        fields = '__all__'
        labels = {
            'id': 'Id',
            'title': 'Titulo',
            'gender': 'Genero',
            'director': 'Director',
            'year': 'Año',
            'sinopsis': 'Sinopsis',
        }
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.NumberInput(attrs={'class': 'form-control'}),
            'director': forms.NumberInput(attrs={'class': 'form-control'}),
            'year': forms.Select(attrs={'class': 'form-control'}),
            'sinopsis': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class userForm(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'age': 'Edad',
            'date': 'Fecha Nacimiento'
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
        }