from datetime import date

from django.test import TestCase

from manager.forms import WorkerRegistrationForm, TaskForm
from manager.models import Position, TaskType, Worker


class FormTests(TestCase):
    def setUp(self):
        self.test_position = Position.objects.create(name="Test Position")
        self.test_task_type = TaskType.objects.create(name="Test Task Type")

    def test_worker_registration_form_is_valid(self):
        form_data = {
            "username": "test_username",
            "password1": "test_pasw1",
            "password2": "test_pasw1",
            "first_name": "test_firstname",
            "last_name": "test_lastname",
            "position": self.test_position,
        }
        form = WorkerRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_task_form_is_valid(self):
        form_data = {
            "name": "Test Create Task",
            "description": "Test Description",
            "deadline": date.today(),
            "is_complete": False,
            "priority": "Urgent",
            "type_of_task": self.test_task_type,
            "assignees": Worker.objects.all(),
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(
            dict(form.cleaned_data["assignees"]), dict(form_data["assignees"])
        )
        del form.cleaned_data["assignees"]
        del form_data["assignees"]
        self.assertEqual(form.cleaned_data, form_data)
