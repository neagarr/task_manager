from django.test import TestCase

from manager.forms import WorkerRegistrationForm
from manager.models import Position


class FormTests(TestCase):

    def test_worker_registration_form_is_valid(self):
        test_position = Position.objects.create(name="Test Position")
        form_data = {
            "username": "test_username",
            "password1": "test_pasw1",
            "password2": "test_pasw1",
            "first_name": "test_firstname",
            "last_name": "test_lastname",
            "position": test_position,
        }
        form = WorkerRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
