from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from manager.models import TaskType, Position, Task


class ModelTests(TestCase):
    def test_task_type_str(self):
        task_type = TaskType.objects.create(name="test")
        self.assertEqual(str(task_type), task_type.name)

    def test_position_str(self):
        position = Position.objects.create(name="test")
        self.assertEqual(str(position), position.name)

    def test_worker_str(self):
        test_position = Position.objects.create(name="test_position")
        worker = get_user_model().objects.create_user(
            username="test_username",
            position=test_position,
            first_name="test_first_name",
            last_name="test_last_name",
        )
        self.assertEqual(
            str(worker),
            f"{worker.position}: {worker.username} "
            f"({worker.first_name} {worker.last_name})",
        )

    def test_create_worker_with_position(self):
        username = "test_username"
        position = Position.objects.create(name="test_position")
        password = "12345jjh"
        worker = get_user_model().objects.create_user(
            username=username, position=position, password=password
        )
        self.assertEqual(worker.username, username)
        self.assertEqual(worker.position, position)
        self.assertTrue(worker.check_password(password))

    def test_task_str(self):
        test_task_type = TaskType.objects.create(name="test_task_type")
        task = Task.objects.create(
            name="test_name",
            description="test_description",
            deadline=datetime.now(),
            priority="test_priority",
            type_of_task=test_task_type,
        )
        self.assertEqual(str(task), task.name)
