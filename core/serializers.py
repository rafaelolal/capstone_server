from rest_framework import serializers
from .models import Unit, Question, Answer

class UnitSerializer(serializers.ModelSerializer):
    answers = AnswerQuestionPKSerializer(many=True, read_only=True)
    
    class Meta:
        model = Unit
        fields = ['key', 'answers']

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
        fields = ['unit', 'question', 'content', 'time_spent']

class AnswerQuestionPKSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['question']

class PeerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['unit', 'content', 'submitted_on']