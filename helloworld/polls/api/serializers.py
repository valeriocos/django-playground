from rest_framework.serializers import ModelSerializer, SerializerMethodField
from ..models import Question, Choice


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class ChoiceSerializer(ModelSerializer):

    question_id = SerializerMethodField('get_question_id')

    class Meta:
        model = Choice
        fields = ['choice_text', 'votes', 'question_id']

    @staticmethod
    def get_question_id(choice):
        return choice.question.id