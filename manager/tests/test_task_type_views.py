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
        self.task_type = TaskType.objects.create(
            name="Test Task Type",
        )
        self.client.force_login(self.user)

    def test_retrieve_task_type_list(self):
        res = self.client.get(TASK_TYPE_LIST_URL)
        self.assertEqual(res.status_code, 200)
        task_types = TaskType.objects.all()
        self.assertEqual(
            list(res.context["task_type_list"]),
            list(task_types),
        )

