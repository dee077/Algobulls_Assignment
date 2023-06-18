from django import forms
from django.utils import timezone
from .models import ToDoItem

class ToDoItemForm(forms.ModelForm):

    class Meta:
        model = ToDoItem
        fields = '__all__'

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date < timezone.now().date():
            raise forms.ValidationError("Due date cannot be in the past.")
        return due_date


