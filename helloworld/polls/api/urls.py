from django.urls import path

from .views import (
    api_list_questions_view,
    api_question_detail_view,
    api_question_create_view,
    api_question_delete_view,
    api_list_choices_view,
    api_choice_detail_view,
    api_choice_create_view,
    api_choice_delete_view,
)

app_name = 'polls'
urlpatterns = [
    path('questions/', api_list_questions_view, name='questions'),
    path('questions/<int:question_id>/', api_question_detail_view, name='question-detail'),
    path('questions/create/', api_question_create_view, name='question-create'),
    path('questions/delete/<int:question_id>/', api_question_delete_view, name='question-delete'),
    path('choices/', api_list_choices_view, name='choices'),
    path('choices/<int:choice_id>/', api_choice_detail_view, name='choice-detail'),
    path('choices/create/', api_choice_create_view, name='choice-create'),
    path('choices/delete/<int:choice_id>/', api_choice_delete_view, name='choice-delete'),
]
