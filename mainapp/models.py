from django.db import models

from django.urls import reverse
from autoslug import AutoSlugField
from django.utils.translation import gettext_lazy as _


class Question(models.Model):

    CHOICES = {
        "what": "what",
        "why": "why",
        "how": "how"
    }

    question = models.CharField(_("Question"), max_length=200)
    question_slug = AutoSlugField(populate_from="question")
    question_category = models.CharField(_("Choices"), choices=CHOICES, max_length=50)
    answer_history = models.JSONField(_("Answers History"), default=dict)

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse("Question_detail", kwargs={"question_slug": self.question_slug})


