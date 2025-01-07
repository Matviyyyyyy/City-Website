
from django.urls import path
from polls import views

urlpatterns = [
    path("questions/", views.QuestionListView.as_view(), name="question-list"),
    path("question/<int:pk>/", views.QuestionDetailView.as_view(), name="question-detail"),
    path("question-create/", views.QuestionCreateView.as_view(), name="question-create"),
    path("question-update/<int:pk>/", views.QuestionUpdateView.as_view(), name="question-update"),
    path("question-delete/<int:pk>/", views.QuestionDeleteView.as_view(), name="question-delete"),
    path("choice-update/<int:pk>/", views.ChoiceUpdateView.as_view(), name="choice-update"),
    path("choice-delete/<int:pk>/", views.ChoiceDeleteView.as_view(), name="choice-delete"),
    path("error-answer/<int:question_id>/", views.error_answer_view, name="error-answer")
]

app_name="polls"