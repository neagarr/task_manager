from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import generic

from .models import Worker, Task, TaskType, Position


def index(request: HttpRequest) -> HttpResponse:
    num_workers = Worker.objects.count()
    num_tasks = Task.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_visits": num_visits,
        "num_workers": num_workers,
        "num_tasks": num_tasks,
    }
    return render(request, "manager/index.html", context=context)


class TaskTypeListView(generic.ListView):
    model = TaskType
    template_name = "manager/task_type_list.html"
    context_object_name = "task_type_list"
    paginate_by = 2


class TaskListView(generic.ListView):
    model = Task
    template_name = "manager/task_list.html"
    context_object_name = "task_list"
    queryset = Task.objects.select_related("type")
    paginate_by = 2


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = "manager/task_detail.html"


class PositionListView(generic.ListView):
    model = Position
    template_name = "manager/position_list.html"
    context_object_name = "position_list"
    paginate_by = 2
