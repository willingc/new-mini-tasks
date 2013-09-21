import unicodecsv
from django.core.management.base import BaseCommand, CommandError
from tasks.models import Task


class Command(BaseCommand):
    args = '<task_csv_filename>'
    help = 'Import a CSV of tasks.'

    def handle(self, *args, **options):
        task_file = csv.DictReader(open(args[0]), encoding='utf-8')

    def _handle_task_file(self, task_file):
        for task in task_file:
            Task.objects.create(
                project=task['Project'],
                url=task['url'],
                item_id=task['itemID'],
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
