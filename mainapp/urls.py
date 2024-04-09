from django.urls import path
from .views import (
    QuestionDetailView
)
from django_distill import distill_path
from .views import questionfunc

urlpatterns = [
    distill_path("<slug:question_slug>/", QuestionDetailView.as_view(), name="Question_detail", distill_func=questionfunc)
]

