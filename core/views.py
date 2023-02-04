from django.shortcuts import render

from .models import Unit, Question, Answer
from rest_framework import viewsets
from .serializers import QuestionSerializer, UnitSerializer, AnswerSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Units to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class UnitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Units to be viewed or edited.
    """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Answers to be viewed or edited.
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer