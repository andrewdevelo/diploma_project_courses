from django.contrib import admin
from apps.enrollment.models import Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'course',
        'enrollment_date',
        'status'
    )
    list_filter = (
        'user',
        'course',
        'enrollment_date',
        'status'
    )
    search_fields = (
        'user',
        'enrollment_date',
    )