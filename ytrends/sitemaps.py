from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from mainapp.models import Video
from django.urls import reverse
from django.http import HttpResponse


class TrendingSitemap(Sitemap):

    changefreq = "daily"
    limit = 50000
    protocol = "https"


    def items(self):
        return Video.objects.all()
    
    def location(self, obj: Model) -> str:
        return reverse("Trendbydate_detail", kwargs={
            "date":obj.date_fetched
        })