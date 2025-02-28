from datetime import datetime, date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import TaskType, Task, Worker

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
        self.test_task_type = TaskType.objects.create(
            name="Test Task Type"
        )
        self.task = Task.objects.create(
            name="Test Task",
            description="Test Description",
            deadline=datetime.now(),
            priority="Urgent",
            type=self.test_task_type
        )
        self.client.force_login(self.user)

    def test_retrieve_task_list(self):
        res = self.client.get(TASK_LIST_URL)
        self.assertEqual(res.status_code, 200)
        tasks = Task.objects.all()
        self.assertEqual(
            list(res.context["task_list"]),
            list(tasks),
        )
        self.assertTemplateUsed(res, "manager/task_list.html")

    def test_retrieve_task_detail(self):
        res = self.client.get(reverse("manager:task_detail", args=[self.task.id]))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "manager/task_detail.html")

    # def test_create_task(self):
    #     print(Task.objects.all())
    #     form_data = {
    #         "name": "Test Create Task",
    #         "description": "Test Description",
    #         "deadline": date.today(),
    #         "is_complete": False,
    #         "priority": "Urgent",
    #         "type": self.test_task_type,
    #         "assignees": Worker.objects.all(),
    #     }
    #     self.client.post(reverse("manager:task_create"), form_data)
    #     print(Task.objects.all())
    #     # new_task = Task.objects.get(name="Test Create")
    #     # print(new_task)
    #
    #     # self.assertEqual(new_task.name, form_data["name"])

    # def test_update_task(self):
    #     task_id = self.task.id
    #     print(Task.objects.all())
    #     form_data = {
    #         "name": "Test Create Task",
    #         "description": "Test Description",
    #         "deadline": date.today(),
    #         "is_complete": False,
    #         "priority": "Urgent",
    #         "type": self.test_task_type,
    #         "assignees": Worker.objects.all(),
    #     }
    #     self.client.post(reverse("manager:task_update", args=[task_id]), form_data)
    #     print(Task.objects.all())
    #     self.assertEqual(Task.objects.get(id=task_id).name, form_data["name"])
    #
    def test_delete_task(self):
        task_id = self.task.id
        self.client.post(reverse("manager:task_delete", args=[task_id]), {})
        self.assertEqual(Task.objects.filter(id=task_id).count(), 0)
