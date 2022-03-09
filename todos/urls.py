from unicodedata import name
from django.urls import path
from .views import (
    BoardListView, 
    TaskAddView, 
    BoardCreateView, 
    BoardDeleteView, 
    BoardDeatilView, 
    ColumnCreateView,
)

urlpatterns = [
    path('new_board/', BoardCreateView.as_view(), name='board_add'),
    path('<int:pk>/', BoardDeatilView.as_view(), name='board_detail'),
    path('<int:pk>/delete/', BoardDeleteView.as_view(), name='board_delete'),
    path('<int:pk>/new_column/', ColumnCreateView.as_view(), name='column_add'),
    path('task/<int:pk>/new/', TaskAddView.as_view(), name='task_add'),
    path('', BoardListView.as_view(), name='board'),
]