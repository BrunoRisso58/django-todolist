from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import TaskModel

class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=256)
    description = forms.CharField(widget=forms.Textarea)
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date < timezone.now().date():
            raise ValidationError("Não é possível selecionar uma data passada.")
        return due_date
    
    class Meta:
        model = TaskModel
        fields = ['title', 'description', 'due_date']