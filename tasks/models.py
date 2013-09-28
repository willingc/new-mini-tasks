import string
from django.db import models


MODE_CHOICES = (
    ('group', 'group'),
    ('individual', 'individual'),
)


class Task(models.Model):
    project = models.CharField(max_length=100)
    item_id = models.CharField(max_length=100)
    url = models.URLField()
    skills = models.CharField(max_length=255)
    community_tools = models.CharField(max_length=255)
    project_area = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    suggested_for = models.CharField(max_length=255)
    closed = models.BooleanField(default=False)
    mentor = models.CharField(max_length=255, default='')
    env_difficulty = models.CharField(max_length=255, default='')
    suggested_mode = models.CharField(
        max_length=25,
        choices=MODE_CHOICES,
    )
    recently_verified = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s (%s)" % (self.summary, self.project)

    def to_dict(self):
        """Return a dict representation of a Task."""

        result = {}
        for field in self._meta.local_fields:
            result[field.name] = getattr(self, field.name)

        # post-process skills
        result['skils'] = map(string.strip, result['skills'].split(','))

        # add any students
        result['students'] = list(
            self.student_set.all().values_list('name', flat=True)
        )

        return result


class Student(models.Model):

    name = models.CharField(max_length=255)
    task = models.ForeignKey(Task)

    def __unicode__(self):
        return "%s working on %s" % (
            self.name,
            self.task,
        )
