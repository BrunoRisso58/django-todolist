from django.shortcuts import render
from django.http import HttpResponse
from .forms import TaskForm

# Create your views here.

def home_page(request):
    return render(request, 'tasksapp/home.html')

def register_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            return HttpResponse('FORMULÁRIO VÁLIDO')
        else:
            print(form.errors)
            return HttpResponse('DEU ERRADO')
        
    return render(request, 'tasksapp/register.html', {'form': TaskForm()})
