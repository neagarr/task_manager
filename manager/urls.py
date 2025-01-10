from django.urls import path
from manager.views import index, TaskTypeListView, TaskListView

urlpatterns = [
    path("", index, name="index"),
    path("task_types/", TaskTypeListView.as_view(), name="task_type_list"),
    path("tasks/", TaskListView.as_view(), name="task_list"),
]

app_name = "manager"
