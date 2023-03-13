from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView
from .serializers import QuestionListSerializer, QuestionSerializer, UnitSerializer, UnitSignedSerializer, AnswerSerializer, PeerReviewSerializer, UnitAnswersListSerializer
from .models import Unit, Question, Answer, PeerReview
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .authentications import CsrfExemptSessionAuthentication

@method_decorator(csrf_exempt, name='dispatch')
class UnitAnswerListView(ListAPIView):
    """
    Retrieves all Units, their classroom, and answers
    """
    authentication_classes = (CsrfExemptSessionAuthentication, )

    queryset = Unit.objects.all()
    serializer_class = UnitAnswersListSerializer
    
@method_decorator(csrf_exempt, name='dispatch')
class QuestionListView(ListAPIView):
    """
    Retrieves all Questions or all non-experiment questions
    """
    authentication_classes = (CsrfExemptSessionAuthentication, )

    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer
    
    def get_queryset(self):
        queryset = Question.objects.all().order_by('opens_on')
        if 'control' in self.kwargs:
            return queryset.exclude(type='Experiment')
        return queryset

@method_decorator(csrf_exempt, name='dispatch')
class QuestionRetrieveView(RetrieveAPIView):
    """
    Retrieves a Question given a primary key.
    """
    authentication_classes = (CsrfExemptSessionAuthentication, )
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

@method_decorator(csrf_exempt, name='dispatch')
class UnitRetrieveView(RetrieveAPIView):
    """
    Retrieves a Unit given a key.
    """
    authentication_classes = (CsrfExemptSessionAuthentication, )
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

@method_decorator(csrf_exempt, name='dispatch')
class UnitSignedView(UpdateAPIView):
    """
    Updates a Unit's signed field to True.
    """
    authentication_classes = (CsrfExemptSessionAuthentication, )
    queryset = Unit.objects.all()
    serializer_class = UnitSignedSerializer

@method_decorator(csrf_exempt, name='dispatch')
class AnswerCreateView(CreateAPIView):
    """
    Creates an Answer.
    """
    authentication_classes = (CsrfExemptSessionAuthentication, )
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

@method_decorator(csrf_exempt, name='dispatch')
class PeerReviewCreateView(CreateAPIView):
    """
    Creates a PeerReview.
    """
    authentication_classes = (CsrfExemptSessionAuthentication, )
    queryset = PeerReview.objects.all()
    serializer_class = PeerReviewSerializer