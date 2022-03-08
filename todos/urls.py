from unicodedata import name
from django.urls import path
from .views import BoardListView, TaskAddView

urlpatterns = [
    path('<int:pk>/new/', TaskAddView.as_view(), name='task_add'),
    path('', BoardListView.as_view(), name='board'),
]