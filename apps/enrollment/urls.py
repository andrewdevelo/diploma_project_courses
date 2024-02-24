from django.urls import path

from apps.enrollment.views import (
    EnrollmentListGenericView,
    RetrieveEnrollmentGenericView
)

urlpatterns = [
    path("", EnrollmentListGenericView.as_view()),
    path("<int:enrollment_id>/", RetrieveEnrollmentGenericView.as_view()),
]