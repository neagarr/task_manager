from datetime import datetime

from django.test import TestCase
from django.urls import reverse

from manager.models import TaskType, Task

TASK_LIST_URL = reverse("manager:task_list")


class PublicTaskTest(TestCase):
    def setUp(self):
        test_type = TaskType.objects.create(
            name="Test Type"
        )
        self.task = Task.objects.create(
            name="Test Task",
            description="Test Description",
            deadline=datetime.now(),
            priority="Urgent",
            type=test_type
        )

    def test_task_list_login_required(self):
        res = self.client.get(TASK_LIST_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_task_detail_login_required(self):
        url = reverse("manager:task_detail", args=[self.task.id])
        res = self.client.get(url)
        self.assertNotEqual(res.status_code, 200)