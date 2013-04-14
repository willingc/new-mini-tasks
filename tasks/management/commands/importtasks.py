import csv
from django.core.management.base import BaseCommand, CommandError
from tasks.models import Task


class Command(BaseCommand):
    args = '<task_csv_filename>'
    help = 'Import a CSV of tasks.'

    def handle(self, *args, **options):
        task_file = csv.DictReader(open(args[0]))

        for task in task_file:
            Task.objects.create(
                project=task['Project'],
                url=task['url'],
                skills=task['Required skills'],
                community_tools=task['Community tools'],
                project_area=task['Project Area'],
                summary=task['Summary'],
                description=task['Description'],
                suggested_for=task['For'],
                closed=bool(task['closed'].strip()),
                suggested_mode=task['suggestedmode'],
                recently_verified=bool(task['recentlyVerified'].strip()),
            )
