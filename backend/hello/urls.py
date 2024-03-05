from django.urls import path

# ============================================================================ #
from .views import HelloList


urlpatterns = [
    path("", HelloList.as_view()),
]
