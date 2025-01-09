from django.urls import path
from manager.views import index, TaskTypeListView

urlpatterns = [
    path("", index, name="index"),
    path("task_types/", TaskTypeListView.as_view(), name="task_type_list"),
]

app_name = "manager"
