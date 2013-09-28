import unicodecsv
from django.core.management.base import BaseCommand
from tasks.models import Task


class Command(BaseCommand):
    args = '<task_csv_filename>'
    help = 'Import a CSV of tasks.'

    def handle(self, *args, **options):
        task_file = unicodecsv.DictReader(open(args[0]), encoding='utf-8')
        return self._handle_task_file(task_file)

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
