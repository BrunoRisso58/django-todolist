from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

class TaskForm(forms.Form):
    task_title = forms.CharField(max_length=256)
    task_description = forms.CharField(widget=forms.Textarea)
    task_due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date < timezone.now().date():
            raise ValidationError("Não é possível selecionar uma data passada.")
        return due_date