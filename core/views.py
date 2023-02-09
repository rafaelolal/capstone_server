from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from .serializers import QuestionListSerializer, QuestionSerializer, UnitSerializer, AnswerSerializer, PeerReviewSerializer
from .models import Unit, Question, Answer, PeerReview

class QuestionListView(ListAPIView):
    """
    Retrieves all Questions or all non-experiment questions
    """
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer
    
    def get_queryset(self):
        queryset = Question.objects.all().order_by('opens_on')
        if 'control' in self.kwargs:
            return queryset.exclude(type='Experiment')
        return queryset

class QuestionRetrieveView(RetrieveAPIView):
    """
    Retrieves a Question given a primary key.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class UnitRetrieveView(RetrieveAPIView):
    """
    Retrieves a Unit given a key.
    """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

class AnswerCreateView(CreateAPIView):
    """
    Creates an Answer.
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class PeerReviewCreateView(CreateAPIView):
    """
    Creates a PeerReview.
    """
    queryset = PeerReview.objects.all()
    serializer_class = PeerReviewSerializer