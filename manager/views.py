from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import generic

from .models import Worker, Task, TaskType


def index(request: HttpRequest) -> HttpResponse:
    num_workers = Worker.objects.count()
    num_tasks = Task.objects.count()
    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks,
    }
    return render(request, "manager/index.html", context=context)


class TaskTypeListView(generic.ListView):
    model = TaskType
    template_name = "manager/task_type_list.html"
    context_object_name = "task_type_list"


class TaskListView(generic.ListView):
    model = Task
    template_name = "manager/task_list.html"
    context_object_name = "task_list"
