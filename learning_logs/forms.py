from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control rounded-3 border-1',
                'rows': 10,
                'placeholder': 'Enter your entry here...'
            }),
        }
            