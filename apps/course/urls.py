from django.urls import path

from apps.course.views import (
    CourseListGenericView,
    RetrieveCourseGenericView,
    CourseListView
)

urlpatterns = [
    path("", CourseListGenericView.as_view()),
    path("<int:course_id>/", RetrieveCourseGenericView.as_view()),
    path("courses_user", CourseListView.as_view())
]
