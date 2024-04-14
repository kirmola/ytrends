from django.urls import path
from .views import (
    TrendByDateDetailView,
    videofunc,
    regions,
)
from django_distill import distill_path

urlpatterns = [
    distill_path("trending-on-<slug:date>/", TrendByDateDetailView.as_view(), name="Trendbydate_detail", distill_func=videofunc)
]

