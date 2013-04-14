from django import forms

import tasks.models


class StudentForm(forms.ModelForm):

    class Meta:
        model = tasks.models.Student
