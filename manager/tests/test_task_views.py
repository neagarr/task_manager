from django.test import TestCase
from django.urls import reverse

TASK_LIST_URL = reverse("manager:task_list")


class PublicTaskTest(TestCase):
    def test_task_list_login_required(self):
        res = self.client.get(TASK_LIST_URL)
        self.assertNotEqual(res.status_code, 200)
