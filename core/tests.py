import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Question, Unit
from .serializers import QuestionSerializer, UnitSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import datetime

# initialize the APIClient app
client = Client()

class GetAllQuestionsTest(TestCase):
    """ Test module for GET all questions API """

    def setUp(self):
        Question.objects.create(
            title="Test", description="Test desc", type="Normal", open_at=datetime.datetime.now(), due_at=datetime.datetime.now())
        Question.objects.create(
            title="Test2", description="Test desc2", type="Posttest", open_at=datetime.datetime.now(), due_at=datetime.datetime.now())
    
    def test_get_all_questions(self):
        # get API response
        response = client.get('/questions/')
        # get data from db
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleQuestionTest(TestCase):
    """ Test module for GET single question API """

    def setUp(self):
        self.test = Question.objects.create(
          title="Test", description="Test desc", type="Normal", open_at=datetime.datetime.now(), due_at=datetime.datetime.now())

    def test_get_valid_single_question(self):
        response = client.get(f'/questions/{self.test.pk}/')
        question = Question.objects.get(pk=self.test.pk)
        serializer = QuestionSerializer(question)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_question(self):
        response = client.get('/questions/30/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

#######################33

class GetAllUnitsTest(TestCase):
    """ Test module for GET all unit API """

    def setUp(self):
        Unit.objects.create(key=1111)
        Unit.objects.create(key=1112)
    
    def test_get_all_units(self):
        # get API response
        response = client.get('/units/')
        # get data from db
        units = Unit.objects.all()
        serializer = UnitSerializer(units, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)