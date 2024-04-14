from django.db import models

from django.urls import reverse
from autoslug import AutoSlugField
from django.utils.translation import gettext_lazy as _

class Video(models.Model):

    video_api_result = models.JSONField(_("API Result"), default=list)
    date_fetched = models.DateField(_("Fetched on:"), default=None, unique=True)

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")

    def __str__(self):
        return f"Youtube Trending on {self.date_fetched}"

    def get_absolute_url(self):
        return reverse("Trendbydate_detail", kwargs={"date": self.date_fetched})
