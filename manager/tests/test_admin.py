from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from manager.models import Position


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="test_admin",
            password="testadmin"
        )
        self.client.force_login(self.admin_user)
        test_position = Position.objects.create(name="Test Worker Position")
        self.worker = get_user_model().objects.create_user(
            username="test_worker",
            password="testworker",
            position=test_position
        )

    def test_worker_position_listed(self):
        """
        Test that the worker position is in list display on worker admin page
        :return:
        """
        url = reverse("admin:manager_worker_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.worker.position.name)
