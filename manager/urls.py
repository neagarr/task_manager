from django.urls import path
from manager.views import (
    index,
    TaskTypeListView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    PositionListView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
)


urlpatterns = [
    path("", index, name="index"),
    path("task_types/", TaskTypeListView.as_view(), name="task_type_list"),
    path("task_types/create/", TaskTypeCreateView.as_view(), name="task_type_create"),
    path("task_types/<int:pk>/update/", TaskTypeUpdateView.as_view(), name="task_type_update"),
    path("task_types/<int:pk>/delete/", TaskTypeDeleteView.as_view(), name="task_type_delete"),
    path("tasks/", TaskListView.as_view(), name="task_list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task_create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path("positions/", PositionListView.as_view(), name="position_list"),
    path("positions/create/", PositionCreateView.as_view(), name="position_create"),
    path("positions/<int:pk>/update/", PositionUpdateView.as_view(), name="position_update"),
    path("positions/<int:pk>/delete/", PositionDeleteView.as_view(), name="position_delete"),
    path("workers/", WorkerListView.as_view(), name="worker_list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker_detail"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker_create"),
]

app_name = "manager"
