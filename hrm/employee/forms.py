from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
            'date_of_joining': forms.DateInput(attrs={'type': 'date'}),
        }
