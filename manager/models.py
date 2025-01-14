from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskType(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Task Type"

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Position"

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        blank=True,
        related_name="workers",
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        ordering = ("username",)
        verbose_name = "Worker"

    def __str__(self):
        return f"{self.position}: {self.username} ({self.first_name} {self.last_name})"


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("Urgent", "Urgent"),
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    ]

    name = models.CharField(max_length=60)
    description = models.TextField()
    deadline = models.DateField()
    is_complete = models.BooleanField(default=False)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE
    )
    assignees = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="tasks",
        blank=True,
    )

    class Meta:
        ordering = ("deadline",)
        verbose_name = "Task"

    def __str__(self):
        return self.name
