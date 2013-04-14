import json
import string
from django.http import HttpResponse
from django.views.generic import (
    FormView,
    TemplateView,
    View,
)

import tasks.forms
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
