from django import forms
from django.db import models
from .models import Comment, Task

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text', 'task')
        widgets = {'task': forms.HiddenInput()}