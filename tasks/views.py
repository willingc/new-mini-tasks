import json
import urllib2
import StringIO
import unicodecsv
from django.http import HttpResponse
from django.views.generic import (
    FormView,
    TemplateView,
    View,
)

import tasks.forms
import tasks.models
import tasks.management.commands.importtasks


class TaskIndex(TemplateView):

    template_name = 'index.html'


class TaskData(View):

    def get(self, request, *args, **kwargs):

        task_data = [
            t.to_dict()
            for t in
            tasks.models.Task.objects.select_related().filter(closed=False)
        ]

        return HttpResponse(
            json.dumps(task_data),
            content_type='application/json',
        )


class ClaimTask(FormView):

    form_class = tasks.forms.StudentForm

    def post(self, request, *args, **kwargs):
        return super(ClaimTask, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()

        return HttpResponse(
            json.dumps({
                'success': True,
            }),
            content_type='application/json',
        )

    def form_invalid(self, form):

        return HttpResponse(
            json.dumps({
                'success': False,
                'errors': form.errors,
            }),
            content_type='application/json',
        )


class RefreshTaskData(View):
    def get(self, request, *args, **kwargs):
        ### Download CSV
        CSV_URL = 'https://docs.google.com/spreadsheet/ccc?key=0AoHP1ey91UqPdC1EUFV4aXBETmY3bFBzTFhpdG1ISEE&output=csv'
        import requests
        response = requests.get(CSV_URL)
        csv_data = response.text
        dr = unicodecsv.DictReader(StringIO.StringIO(csv_data), encoding='utf-8')

        ### Assuming we actually got the data, delete all tasks currently
        tasks.models.Task.objects.all().delete()

        ### Load the new ones in
        tasks.management.commands.importtasks.Command()._handle_task_file(dr)

        ### Exit successfully.
        return HttpResponse("Refreshed task data.")
