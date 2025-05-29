# views.py
from django.shortcuts import render, redirect
from .models import Todopage


def todo(request):
    if request.method == 'POST':
        task = request.POST.get('tasks')  # Get task from the POST data

        if task:
            Todopage.objects.create(tasks=task)  # Create a new task

        return redirect('todo')  # Reload the page after submitting

    # Fetch all tasks
    tasks = Todopage.objects.all()
    return render(request, 'app/todo.html', {'tasks': tasks})


def mark_completed(request, task_id):
    task = Todopage.objects.get(id=task_id)
    task.completed = not task.completed  # Toggle the completion status
    task.save()
    return redirect('todo')


def delete_task(request, task_id):
    task = Todopage.objects.get(id=task_id)
    task.delete()
    return redirect('todo')
