from django.contrib import admin

from apps.course.models import Course
from apps.user.models import User


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'end_date', 'instructor')
    list_filter = ('title', 'description', 'start_date', 'end_date', 'instructor')
    search_fields = ('title',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'instructor':
            kwargs["queryset"] = User.objects.filter(is_instructor=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
