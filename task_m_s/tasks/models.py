from django.contrib.auth.models import User
from django.db import models

class Label(models.Model):
    name = models.CharField(max_length=50, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        # Ensure that each label name is unique per owner
        unique_together = ['name', 'owner']

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completion_status = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    labels = models.ManyToManyField(Label)

    def __str__(self):
        return self.title
