from django.urls import path
from .views import (
    QuestionDetailView,
    questionfunc,
)
from django_distill import distill_path

urlpatterns = [
    distill_path("<slug:question_slug>/", QuestionDetailView.as_view(), name="Question_detail", distill_func=questionfunc)
]

