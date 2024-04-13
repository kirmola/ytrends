from django.urls import path
from .views import (
    VideoDetailView,
    videofunc,
    regions,
)
from django_distill import distill_path

urlpatterns = [
    # distill_path("trending-on-<int:date>-<int:month>-<int:year>/", VideoDetailView.as_view(), name="Trend_detail", distill_func=videofunc)
]

