from django.contrib import admin

# Register your models here.
from django.contrib import admin
from todo.models import Task

admin.site.register(Task)