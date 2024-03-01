from django.urls import path
from apps.online_courses.views import (
    home_page,
    get_all_courses,
    create_new_course,
    get_course_info_by_course_id,
    update_course,
    delete_course,
)

urlpatterns = [
    path("", home_page, name='home'),
    path("allcourses/", get_all_courses, name='all-courses'),
    path("create/", create_new_course, name='create-course'),
    path("<int:course_id>/", get_course_info_by_course_id, name='course-info'),
    path("<int:course_id>/update/", update_course, name='update-course'),
    path("<int:course_id>.delete/", delete_course, name='delete-course'),
]