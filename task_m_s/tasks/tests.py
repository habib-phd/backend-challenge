from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Task, Label

class TaskModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.task = Task.objects.create(title='Test Task', description='Test Description', owner=self.user)

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'Test Description')
        self.assertEqual(self.task.owner, self.user)

class TaskAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.task = Task.objects.create(title='Test Task', description='Test Description', owner=self.user)

    def test_task_list(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_task_detail(self):
        response = self.client.get(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test Task')

    # Add more tests for create, update, and delete operations as needed

class LabelModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.label = Label.objects.create(name='Test Label', owner=self.user)

    def test_label_creation(self):
        self.assertEqual(self.label.name, 'Test Label')
        self.assertEqual(self.label.owner, self.user)

class LabelAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.label = Label.objects.create(name='Test Label', owner=self.user)

    def test_label_list(self):
        response = self.client.get('/api/labels/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_label_detail(self):
        response = self.client.get(f'/api/labels/{self.label.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Label')
