from rest_framework import serializers
from .models import Unit, Question, Answer, PeerReview

class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['pk', 'title', 'opens_on', 'due_on', 'type', 'pre_requisite']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['title', 'description', 'type']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['unit', 'question', 'content', 'time_spent']

class AnswerQuestionPKSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['question']

class UnitSerializer(serializers.ModelSerializer):
    answers = AnswerQuestionPKSerializer(many=True, read_only=True)
    
    class Meta:
        model = Unit
        fields = ['key', 'signed', 'answers', 'type']

class UnitSignedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['signed']

class PeerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeerReview
        fields = ['unit', 'content', 'submitted_on']