from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "Task Type"

    def __str__(self):
        return self.name


class Worker(AbstractUser):

    class Meta:
        ordering = ("username",)
        verbose_name = "Worker"


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    deadline = models.DateField()
    is_complete = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="tasks")

    class Meta:
        ordering = ("deadline",)
        verbose_name = "Task"

    def __str__(self):
        return self.name
