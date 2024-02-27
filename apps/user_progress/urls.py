from django.urls import path

from apps.user_progress.views import (
    UserProgressListGenericView,
    RetrieveUserProgressGenericView
)

urlpatterns = [
    path("", UserProgressListGenericView.as_view()),
    path("<int:progress_id>/", RetrieveUserProgressGenericView.as_view()),
]
