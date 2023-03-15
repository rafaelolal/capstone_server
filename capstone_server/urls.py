"""capstone_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('unit/<int:pk>/', csrf_exempt(views.UnitRetrieveView.as_view()),
         name="unit_retrieve"),
    path('unit-answers/', csrf_exempt(views.UnitAnswerListView.as_view()),
         name="unit_answers"),
    path('unit-signed/<int:pk>/',
         csrf_exempt(views.UnitSignedView.as_view()), name="unit_signed"),
    path('question-list/', csrf_exempt(views.QuestionListView.as_view()),
         name="question_list"),
    path('question/<int:pk>/', csrf_exempt(views.QuestionRetrieveView.as_view()),
         name="question_retrieve"),
    path('feedback/<int:pk>/', csrf_exempt(views.FeedbackRetrieveView.as_view()),
         name="feedback_retrieve"),
    path('answer/', csrf_exempt(views.AnswerCreateView.as_view()),
         name="answer_create"),
    path('peer-review/', csrf_exempt(views.PeerReviewCreateView.as_view()),
         name="peer_review_create"),
    path('admin/', admin.site.urls),
]
