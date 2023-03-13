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