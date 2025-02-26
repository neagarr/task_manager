from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import TaskType, Task

TASK_LIST_URL = reverse("manager:task_list")


class PublicTaskTest(TestCase):
    def setUp(self):
        test_task_type = TaskType.objects.create(
            name="Test Task Type"
        )
        self.task = Task.objects.create(
            name="Test Task",
            description="Test Description",
            deadline=datetime.now(),
            priority="Urgent",
            type=test_task_type
        )

    def test_task_list_login_required(self):
        res = self.client.get(TASK_LIST_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_task_detail_login_required(self):
        url = reverse("manager:task_detail", args=[self.task.id])
        res = self.client.get(url)
        self.assertNotEqual(res.status_code, 200)


class PrivateTaskTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="test_password",
        )
        test_task_type = TaskType.objects.create(
            name="Test Task Type"
        )
        self.task = Task.objects.create(
            name="Test Task",
            description="Test Description",
            deadline=datetime.now(),
            priority="Urgent",
            type=test_task_type
        )
        self.client.force_login(self.user)

    def test_retrieve_worker_list(self):
        res = self.client.get(TASK_LIST_URL)
        self.assertEqual(res.status_code, 200)
        tasks = Task.objects.all()
        self.assertEqual(
            list(res.context["task_list"]),
            list(tasks),
        )
        self.assertTemplateUsed(res, "manager/task_list.html")

    def test_retrieve_worker_detail(self):
        res = self.client.get(reverse("manager:task_detail", args=[self.task.id]))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "manager/task_detail.html")
