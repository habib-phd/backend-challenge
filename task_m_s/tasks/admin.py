from django.contrib import admin

# Register your models here.
from .models import Task, Label

admin.site.register(Task)
admin.site.register(Label)
