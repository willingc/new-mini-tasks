from django.contrib import admin
from tasks.models import (
    Task,
    Student,
)

admin.site.register(Task)
admin.site.register(Student)
