from rest_framework import serializers
from .models import Unit, Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['title', 'description', 'open_at', 'due_at', 'type']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['unit_id', 'question_id', 'response', 'time_spent']

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['key']