from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import TaskType

TASK_TYPE_LIST_URL = reverse("manager:task_type_list")


class PublicTaskTypeTest(TestCase):

    def test_task_type_login_required(self):
        res = self.client.get(TASK_TYPE_LIST_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTaskTypeTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="testpassword",
        )
        self.task_type = TaskType.objects.create(name="Test Task Type", )
        self.client.force_login(self.user)

    def test_retrieve_task_type_list(self):
        res = self.client.get(TASK_TYPE_LIST_URL)
        self.assertEqual(res.status_code, 200)
        task_types = TaskType.objects.all()
        self.assertEqual(
            list(res.context["task_type_list"]),
            list(task_types),
        )

    def test_create_task_type(self):
        form_data = {"name": "Test Create"}
        self.client.post(reverse("manager:task_type_create"), form_data)
        new_task_type = TaskType.objects.get(name="Test Create")

        self.assertEqual(new_task_type.name, form_data["name"])

    def test_update_task_type(self):
        task_type_id = self.task_type.id
        form_data = {"name": "Test Update"}
        self.client.post(
            reverse("manager:task_type_update", args=[task_type_id]),
            form_data
        )
        self.assertEqual(
            TaskType.objects.get(id=task_type_id).name,
            form_data["name"]
        )

    def test_delete_task_type(self):
        task_type_id = self.task_type.id
        self.client.post(
            reverse("manager:task_type_delete", args=[task_type_id]),
            {}
        )
        self.assertEqual(TaskType.objects.filter(id=task_type_id).count(), 0)
