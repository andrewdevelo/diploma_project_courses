from django.forms import (
    ModelForm,
    fields,
    ModelChoiceField,
    widgets,
)

from apps.user.models import User
from apps.course.models import Course


class CreateCourseForm(ModelForm):
    title = fields.CharField(max_length=100)
    description = fields.CharField(
        max_length=1500,
        widget=fields.Textarea
    )
    start_date = fields.DateTimeField(
        localize=True,
        widget=widgets.DateTimeInput(
            format=('%Y-%m-%dT%H:%M'),
            attrs={'type': 'datetime-local'}
        )
    )
    end_date = fields.DateTimeField(
        localize=True,
        widget=widgets.DateTimeInput(
            format=('%Y-%m-%dT%H:%M'),
            attrs={'type': 'datetime-local'}
        )
    )
    instructor = ModelChoiceField(
        queryset=User.objects.filter(is_instructor=True)
    )

    class Meta:
        model = Course
        fields = '__all__'


class CourseUpdateForm(ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'start_date', 'end_date', 'instructor')