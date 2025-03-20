from django import forms
from .models import Trainee

class TraineeForm(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = ['name', 'email', 'phone', 'course', 'image']
