from django.urls import path
from manager.views import (
    index,
    TaskTypeListView,
    TaskListView,
    PositionListView,
    TaskDetailView,
    WorkerListView)


urlpatterns = [
    path("", index, name="index"),
    path("task_types/", TaskTypeListView.as_view(), name="task_type_list"),
    path("tasks/", TaskListView.as_view(), name="task_list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("positions/", PositionListView.as_view(), name="position_list"),
    path("workers/", WorkerListView.as_view(), name="worker_list"),
]

app_name = "manager"
