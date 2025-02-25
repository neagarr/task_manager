from django.test import TestCase
from django.urls import reverse

WORKER_LIST_URL = reverse("manager:worker_list")


class PublicWorkerTest(TestCase):
    def test_worker_list_login_required(self):
        res = self.client.get(WORKER_LIST_URL)
        self.assertNotEqual(res.status_code, 200)