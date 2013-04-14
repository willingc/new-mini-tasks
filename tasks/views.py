import json
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
