from django.urls import path
from apps.online_courses.views import home_page


urlpatterns = [
    path("", home_page),
]