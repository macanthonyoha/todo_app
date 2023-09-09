
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task


# Create your views here.

def addTask(request):
    # saving task to our database from here
    task = request.POST['task']
    Task.objects.create(task=task)
    #we want after entering the task and we click on add it takes me back to home page.
    return redirect('home')

