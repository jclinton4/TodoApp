from django import forms
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Board, Label, Column, Task

class TaskUpdateForm(forms.ModelForm):
    column = forms.CharField(max_length=50, disabled=False)

    class Meta:
        model = Task
        fields = '__all__'

class BoardListView(ListView):
    model = Board
    template_name = 'board.html'

class BoardDeatilView(DetailView):
    model = Board
    template_name = 'board_detail.html'

class BoardDeleteView(DeleteView):
    model = Board
    template_name = 'board_delete.html'
    success_url = reverse_lazy('board')

class BoardCreateView(CreateView):
    model = Board
    template_name = 'board_new.html'
    fields = '__all__'

class ColumnCreateView(CreateView):
    model = Column
    template_name = 'column_new.html'
    fields = '__all__'

class TaskAddView(CreateView):
    model = Task
    template_name = 'task_add.html'
    fields = ('title', 'column', 'description', 'priority')
    #form_class = TaskUpdateForm
    
