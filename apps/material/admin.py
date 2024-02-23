from django.contrib import admin
from apps.material.models import Material


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content_text',
        'content_file',
        'module'
    )
    list_filter = (
        'title',
        'content_text',
        'content_file',
        'module'
    )
    search_fields = ('title',)
