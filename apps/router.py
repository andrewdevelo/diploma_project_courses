from django.urls import include, path

urlpatterns = [
    path('users/', include('apps.user.urls')),
    path('courses/', include('apps.course.urls')),
    path('modules/', include('apps.module.urls')),
    path('materials/', include('apps.material.urls')),
    path('enrollments/', include('apps.enrollment.urls')),
    path('progress/', include('apps.user_progress.urls')),
    path('', include('apps.online_courses.urls'))
]
