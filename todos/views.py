from xml.etree.ElementTree import Comment
from django import forms
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import UpdateView, DeleteView, CreateView, FormMixin
from django.urls import reverse_lazy, reverse

from .models import Board, Label, Column, Task, Comment
from .forms import CommentForm

class TaskUpdateForm(forms.ModelForm):
    column = forms.CharField(max_length=50, disabled=False)

    class Meta:
        model = Task
        fields = '__all__'

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
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

class ColumnDeleteView(DeleteView):
    model = Column
    template_name = 'column_delete.html'

    def get_success_url(self):
        board_id = self.kwargs['pk']
        return reverse_lazy('board_detail')

class TaskAddView(CreateView):
    model = Task
    template_name = 'task_add.html'
    fields = ('title', 'column', 'description', 'priority')
    #form_class = TaskUpdateForm
    
class TaskDetailView(FormMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk', self.object.id})
    
    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'task': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        form.save()
        return super(TaskDetailView, self).form_valid(form)
