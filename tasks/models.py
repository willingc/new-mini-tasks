from django.db import models


MODE_CHOICES = (
    ('group', 'group'),
    ('individual', 'individual'),
)


class Task(models.Model):
    project = models.CharField(max_length=100)
    url = models.URLField()
    skills = models.CharField(max_length=255)
    community_tools = models.CharField(max_length=255)
    project_area = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    suggested_for = models.CharField(max_length=255)
    closed = models.BooleanField(default=False)
    suggested_mode = models.CharField(
        max_length=25,
        choices=MODE_CHOICES,
    )
    recently_verified = models.BooleanField(default=False)


class Student(models.Model):

    name = models.CharField(max_length=255)
    task = models.ForeignKey(Task)
