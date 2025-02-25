from django.test import TestCase
from django.urls import reverse

POSITION_LIST_URL = reverse("manager:position_list")


class PublicPositionTest(TestCase):
    def test_position_list_login_required(self):
        res = self.client.get(POSITION_LIST_URL)
        self.assertNotEqual(res.status_code, 200)