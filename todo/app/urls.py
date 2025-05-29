# urls.py
from django.urls import path
from .views import todo, mark_completed, delete_task

urlpatterns = [
    path('', todo, name='todo'),  # Main page with the tasks
    path('mark_completed/<int:task_id>/', mark_completed,
         name='mark_completed'),  # Mark task as completed
    path('delete_task/<int:task_id>/', delete_task,
         name='delete_task'),  # Delete task
]
