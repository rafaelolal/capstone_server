from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from .serializers import QuestionListSerializer, QuestionSerializer, UnitSerializer, AnswerSerializer
from .models import Unit, Question, Answer

class QuestionListView(ListAPIView):
    """
    API endpoint that allows Questions to be retrieved.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer

class QuestionRetrieveView(RetrieveAPIView):
    """
    API endpoint that allows a Question to be retrieved.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class UnitRetrieveView(RetrieveAPIView):
    """
    API endpoint that allows a Unit to be retrieved.
    """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

# TODO: add protection/permissions
class AnswerCreateView(CreateAPIView):
    """
    API endpoint that allows an Answer to be created.
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer