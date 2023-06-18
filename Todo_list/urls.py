from django.urls import path
from .views import ToDoItemListCreateView, ToDoItemRetrieveUpdateDestroyView

urlpatterns = [
    path('api/todo/', ToDoItemListCreateView.as_view(), name='todo-list-create'),
    path('api/todo/<int:pk>/', ToDoItemRetrieveUpdateDestroyView.as_view(), name='todo-retrieve-update-destroy'),
]