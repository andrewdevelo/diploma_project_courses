from django.urls import path
from apps.online_courses.views import (
    home_page,
    get_all_courses,
)


urlpatterns = [
    path("", home_page),
    path("allcourses/", get_all_courses),

]