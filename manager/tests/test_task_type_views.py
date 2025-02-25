from django.test import TestCase, Client
from django.urls import reverse

TASK_TYPE_LIST_URL = reverse("manager:task_type_list")


class PublicTaskTypeTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(TASK_TYPE_LIST_URL)
        self.assertNotEqual(res.status_code, 200)


