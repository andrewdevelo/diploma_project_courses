from django.contrib import admin
from apps.user_progress.models import UserProgress


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'course',
        'module',
        'progress',
        'last_update'
    )
    list_filter = (
        'user',
        'course',
        'module',
        'progress',
        'last_update'
    )
    search_fields = (
        'user',
        'progress',
    )
