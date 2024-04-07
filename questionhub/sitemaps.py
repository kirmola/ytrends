from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from mainapp.models import Question
from django.urls import reverse


class QuestionSitemap(Sitemap):

    changefreq = "daily"
    limit = 50000
    protocol = "https"


    def items(self):
        return Question.objects.all()
    
    def location(self, obj: Model) -> str:
        return reverse("Question_detail", kwargs={
            "question_slug":obj.question_slug
        })
    
    