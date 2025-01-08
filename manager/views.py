from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Worker, Task


def index(request: HttpRequest) -> HttpResponse:
    num_workers = Worker.objects.count()
    num_tasks = Task.objects.count()
    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks,
    }

    return render(request, 'manager/index.html', context=context)
