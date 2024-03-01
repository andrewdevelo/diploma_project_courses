from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from apps.course.models import Course
from apps.user.models import User
from apps.module.models import Module
from apps.material.models import Material
from apps.online_courses.forms import (
    CreateCourseForm,
    CourseUpdateForm
)


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


def create_new_course(request):
    users = User.objects.filter(is_instructor=True)

    if request.method == 'POST':
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            course_data = form.cleaned_data
            Course.objects.create(**course_data)
            return redirect('all-courses')

        context = {
            "form": form,
            "users": users
        }
    else:
        form = CreateCourseForm()
        context = {
            "form": form,
            "users": users
        }
    return render(
        request=request,
        template_name='online_courses/create_course.html',
        context=context
    )


def update_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    users = User.objects.filter(is_instructor=True)

    if request.method == 'POST':
        form = CourseUpdateForm(request.POST, instance=course)

        if form.is_valid():
            form.save()
            return redirect('all-courses')

        context = {
            "form": form,
            "course": course,
            "users": users,
        }
    else:
        form = CourseUpdateForm(instance=course)

        context = {
            "form": form,
            "course": course,
            "users": users,
        }

    return render(
        request=request,
        template_name='online_courses/update_course.html',
        context=context
    )


def get_course_info_by_course_id(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    context = {
        "course": course,
    }

    return render(
        request=request,
        template_name='online_courses/course_info.html',
        context=context
    )


def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    course.delete()
    return redirect('all-courses')
