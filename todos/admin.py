from django.contrib import admin

from .models import Board, Label, Column, Task

admin.site.register(Board)
admin.site.register(Label)
admin.site.register(Column)
admin.site.register(Task)
