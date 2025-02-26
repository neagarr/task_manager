from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from manager.models import Position

POSITION_LIST_URL = reverse("manager:position_list")


class PublicPositionTest(TestCase):
    def test_position_list_login_required(self):
        res = self.client.get(POSITION_LIST_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivatePositionTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="testpassword",
        )
        self.position = Position.objects.create(name="Test Position",)
        self.client.force_login(self.user)

    def test_retrieve_position_list(self):
        res = self.client.get(POSITION_LIST_URL)
        self.assertEqual(res.status_code, 200)
        positions = Position.objects.all()
        self.assertEqual(
            list(res.context["position_list"]),
            list(positions),
        )
        self.assertTemplateUsed(res, "manager/position_list.html")
