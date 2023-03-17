from rest_framework import serializers
from .models import Unit, Question, Answer, Feedback, PeerReview


class UnitMissingCountListSerializer(serializers.ModelSerializer):
    classroom = serializers.SerializerMethodField()
    missing = serializers.SerializerMethodField()

    class Meta:
        model = Unit
        fields = ['key', 'classroom', 'missing']

    def get_classroom(self, obj):
        if (obj.classroom):
            return obj.classroom.period
        return None

    def get_missing(self, obj):
        total_questions = Question.objects.count()
        if obj.type == 'Experimental':
            return total_questions - obj.answers.count()
        return 2 - obj.answers.count()


class FeedbackListSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Feedback
        fields = ['questions']

    def get_questions(self, obj):
        return Feedback.objects.all().values_list('question')


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['pk', 'title', 'opens_on', 'due_on', 'type', 'pre_requisite']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['title', 'description', 'type']


class FeedbackSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = Feedback
        fields = ['description', 'title', 'question']

    def get_title(self, obj):
        return obj.question.title


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
