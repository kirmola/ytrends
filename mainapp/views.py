from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Video
from django.views.generic import DetailView


class TrendByCountryDetailView(DetailView):
    model = Video
    template_name = "mainapp/ytrends_tbc.html"
    slug_url_kwarg = "cc"
    slug_field = "trending_cc"

    def get_queryset(self):
        country_in_url = self.kwargs.get("cc")
        print(super().get_queryset().filter(trending_cc=country_in_url).query)
        return super().get_queryset().filter(trending_cc=country_in_url)


def videofunc():
    for eachquestion in Video.objects.all():
        yield {
            "question_slug": eachquestion.question_slug
        }


def regions():
    pass