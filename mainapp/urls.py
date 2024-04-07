from django.urls import path
from .views import (
    QuestionDetailView
)

urlpatterns = [
    path("<slug:question_slug>/", QuestionDetailView.as_view(), name="Question_detail")
]
