from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Video
from django.views.generic import DetailView


class TrendByDateDetailView(DetailView):
    model = Video
    template_name = "mainapp/index.html"
    slug_url_kwarg = "date"
    slug_field = "date_fetched"

    def get_queryset(self):
        date_in_url = self.kwargs.get("date_fetched")
        return super().get_queryset().filter(date_fetched=date_in_url)


def videofunc():
    for eachquestion in Video.objects.all():
        yield {
            "question_slug": eachquestion.question_slug
        }


def regions():
    pass