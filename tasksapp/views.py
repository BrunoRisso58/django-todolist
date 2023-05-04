from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskForm
from .models import TaskModel
from datetime import date

# Create your views here.

def home_page(request):
    tasks = TaskModel.objects.filter(due_date=date.today())
    return render(request, 'tasksapp/home.html', {'tasks': tasks})

def all_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'tasksapp/tasks.html', {'tasks': tasks})

def register_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            messages.success(request, 'Tarefa registrada com sucesso!')
            return redirect('/cadastro')
        else:
            messages.error(request, 'Error: {}'.format(form.errors))
    else:
        form = TaskForm()
        
    return render(request, 'tasksapp/register.html', {'form': TaskForm()})
