from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task


def home(request):
                                                 # the .order_by('updated_at') is to arrange the task on the webpage
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    # now we don't want to print tasks, but we want this to display on our front page, we are going to delete print
    context = {
        'tasks': tasks,
    }
    return render(request, 'home.html', context)
