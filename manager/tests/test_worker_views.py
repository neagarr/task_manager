
from django.contrib.auth import get_user_model

from django.test import TestCase
from django.urls import reverse

from manager.models import Worker

WORKER_LIST_URL = reverse("manager:worker_list")


class PublicWorkerTest(TestCase):
    def setUp(self):
        self.worker = Worker.objects.create(
            username="Test Worker",
            password="<PASSWORD>",
        )

    def test_worker_list_login_required(self):
        res = self.client.get(WORKER_LIST_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_worker_detail_login_required(self):
        url = reverse("manager:worker_detail", args=[self.worker.id])
        res = self.client.get(url)
        self.assertNotEqual(res.status_code, 200)


class PrivateWorkerTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="testpassword",
        )
        self.worker = Worker.objects.create(
            username="Test Worker",
            password="<PASSWORD>",
        )
        self.client.force_login(self.user)

    def test_retrieve_worker_list(self):
        res = self.client.get(WORKER_LIST_URL)
        self.assertEqual(res.status_code, 200)
        workers = Worker.objects.all()
        self.assertEqual(
            list(res.context["worker_list"]),
            list(workers),
        )
        self.assertTemplateUsed(res, "manager/worker_list.html")

    def test_retrieve_worker_detail(self):
        res = self.client.get(reverse("manager:worker_detail", args=[self.worker.id]))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "manager/worker_detail.html")
