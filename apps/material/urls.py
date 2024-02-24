from django.urls import path

from apps.material.views import (
    MaterialListGenericView,
    RetrieveMaterialGenericView
)

urlpatterns = [
    path("", MaterialListGenericView.as_view()),
    path("<int:material_id>/", RetrieveMaterialGenericView.as_view()),
]