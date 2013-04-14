import json
import string
from django.http import HttpResponse
from django.views.generic import (
    TemplateView,
    View,
)

import tasks.models


class TaskIndex(TemplateView):

    template_name = 'index.html'


class TaskData(View):

    def get(self, request, *args, **kwargs):

        task_data = list(
            tasks.models.Task.objects.filter(closed=False).values()
        )
        for task in task_data:
            task['skills'] = map(string.strip, task['skills'].split(','))

        return HttpResponse(
            "var example_items = %s;\n" % json.dumps(task_data),
            content_type='text/javascript',
        )
