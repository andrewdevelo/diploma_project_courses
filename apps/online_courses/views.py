from django.shortcuts import render
from apps.course.models import Course


def home_page(request):
    return render(
        request=request,
        template_name='main.html'
    )


def get_all_courses(request):
    courses = Course.objects.all()

    context = {
        'courses': courses
    }

    return render(
        request=request,
        template_name='online_courses/all_courses.html',
        context=context
    )
