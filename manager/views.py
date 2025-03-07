from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required

from .forms import WorkerRegistrationForm, TaskForm
from .mixins import QuerysetMixin, ContextMixin
from .models import Worker, Task, TaskType, Position


@login_required()
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


class TaskTypeListView(
    LoginRequiredMixin,
    QuerysetMixin,
    ContextMixin,
    generic.ListView
):
    model = TaskType
    template_name = "manager/task_type_list.html"
    context_object_name = "task_type_list"
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskTypeListView, self).get_context_data(**kwargs)
        return self.get_context_data_mixin(context)

    def get_queryset(self):
        queryset = TaskType.objects.all()
        return self.get_queryset_mixin(queryset)


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("manager:task_type_list")
    template_name = "manager/task_type_form.html"


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("manager:task_type_list")
    template_name = "manager/task_type_form.html"


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    template_name = "manager/task_type_confirm_delete.html"
    success_url = reverse_lazy("manager:task_type_list")


class TaskListView(
    LoginRequiredMixin,
    QuerysetMixin,
    ContextMixin,
    generic.ListView
):
    model = Task
    template_name = "manager/task_list.html"
    context_object_name = "task_list"
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        return self.get_context_data_mixin(context)

    def get_queryset(self):
        queryset = Task.objects.select_related("type_of_task")
        return self.get_queryset_mixin(queryset)


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "manager/task_detail.html"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    success_url = reverse_lazy("manager:task_list")
    template_name = "manager/task_form.html"
    form_class = TaskForm


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    success_url = reverse_lazy("manager:task_list")
    template_name = "manager/task_form.html"
    form_class = TaskForm


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("manager:task_list")
    template_name = "manager/task_confirm_delete.html"


class PositionListView(
    LoginRequiredMixin,
    QuerysetMixin,
    ContextMixin,
    generic.ListView
):
    model = Position
    template_name = "manager/position_list.html"
    context_object_name = "position_list"
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PositionListView, self).get_context_data(**kwargs)
        return self.get_context_data_mixin(context)

    def get_queryset(self):
        queryset = Position.objects.all()
        return self.get_queryset_mixin(queryset)


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("manager:position_list")
    template_name = "manager/position_form.html"


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("manager:position_list")
    template_name = "manager/position_form.html"


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("manager:position_list")
    template_name = "manager/position_confirm_delete.html"


class WorkerListView(
    LoginRequiredMixin,
    QuerysetMixin,
    ContextMixin,
    generic.ListView
):
    model = Worker
    template_name = "manager/worker_list.html"
    context_object_name = "worker_list"
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        return self.get_context_data_mixin(context)

    def get_queryset(self):
        queryset = Worker.objects.select_related("position")
        return self.get_queryset_mixin(queryset)


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    template_name = "manager/worker_detail.html"


def register(request):
    if request.method == "GET":
        form = WorkerRegistrationForm()
        return render(request, "manager/worker_form.html", {'form': form})
    if request.method == 'POST':
        form = WorkerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "You have registered successfully.")
            login(request, user)
            return redirect("manager:index")
        else:
            return render(request, "manager/worker_form.html", {'form': form})
