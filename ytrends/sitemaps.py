from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from mainapp.models import Video
from django.urls import reverse
from django.http import HttpResponse
from datetime import datetime

class TrendingSitemap(Sitemap):

    limit = 50000
    protocol = "https"


    def items(self):
        return Video.objects.all()
    
    def location(self, obj: Model) -> str:
        return reverse("Trendbycountry_detail", kwargs={
            "cc":obj.trending_cc.country_code
        })
    
    def lastmod(self, obj):
        return datetime.now()