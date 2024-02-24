from django.contrib import admin
from apps.module.models import Module


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'course')
    list_filter = ('title', 'description', 'course')
    search_fields = ('title',)
