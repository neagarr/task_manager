from django.urls import path
from manager.views import index, task_type_list_view

urlpatterns = [
    path("", index, name="index"),
    path("task_types/", task_type_list_view, name="task_type_list"),
]

app_name = "manager"
