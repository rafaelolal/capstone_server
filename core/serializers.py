from rest_framework import serializers
from .models import Unit, Question, Answer

class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['pk', 'title', 'open_at', 'due_at', 'type']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['title', 'description']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['unit_id', 'question_id', 'content', 'time_spent']

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['key']