from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer


@api_view(['GET', ])
def api_list_questions_view(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)

    return Response(serializer.data)


@api_view(['POST', ])
def api_question_create_view(request):
    serializer = QuestionSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(status.HTTP_400_BAD_REQUEST)

    Question.objects.create(**request.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE', ])
def api_question_delete_view(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    question.delete()
    return Response(f"Question {question_id} deleted")


@api_view(['GET', ])
def api_question_detail_view(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = QuestionSerializer(question)
    return Response(serializer.data)


@api_view(['GET', ])
def api_list_choices_view(request):
    choices = Choice.objects.all()
    serializer = ChoiceSerializer(choices, many=True)

    return Response(serializer.data)


@api_view(['POST', ])
def api_choice_create_view(request):
    try:
        question = Question.objects.get(id=request.data["question_id"])
    except Question.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ChoiceSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(status.HTTP_400_BAD_REQUEST)

    choice = Choice.objects.create(question=question, votes=serializer.validated_data['votes'], choice_text=serializer.validated_data['choice_text'])

    # to be improved
    model_dict_instance = {"question_id": choice.question.id, "votes": choice.votes, "choice_text": choice.choice_text}
    return Response(model_dict_instance, status=status.HTTP_201_CREATED)


@api_view(['GET', ])
def api_choice_detail_view(request, choice_id):
    try:
        choice = Choice.objects.get(id=choice_id)
    except Choice.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ChoiceSerializer(choice)
    return Response(serializer.data)


@api_view(['DELETE', ])
def api_choice_delete_view(request, choice_id):
    try:
        choice = Choice.objects.get(id=choice_id)
    except Choice.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    choice.delete()
    return Response(f"Choice {choice_id} deleted")

