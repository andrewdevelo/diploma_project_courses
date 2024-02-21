from django.urls import path

from apps.module.views import (
    ModuleListGenericView,
    RetrieveModuleGenericView
)

urlpatterns = [
    path("", ModuleListGenericView.as_view()),
    path("<int:module_id>/", RetrieveModuleGenericView.as_view()),
]
