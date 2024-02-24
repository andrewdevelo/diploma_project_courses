from django.urls import include, path

urlpatterns = [
    path('users/', include('apps.user.urls')),
    path('courses/', include('apps.course.urls')),
    path('modules/', include('apps.module.urls')),
]
