from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import QuestionListSerializer, QuestionSerializer, UnitSerializer, AnswerSerializer
from .models import Unit, Question, Answer

class QuestionListView(ListAPIView):
    """
    API endpoint that allows Questions to be retrieved.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer
    permission_classes = (IsAuthenticated,)

class QuestionRetrieveView(RetrieveAPIView):
    """
    API endpoint that allows a Question to be retrieved.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.kwargs['control']:
            return Question.objects.exclude(type='Normal')
        return Question.objects.all()

class UnitRetrieveView(RetrieveAPIView):
    """
    API endpoint that allows a Unit to be retrieved.
    """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = (IsAuthenticated,)

class AnswerCreateView(CreateAPIView):
    """
    API endpoint that allows an Answer to be created.
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (IsAuthenticated,)