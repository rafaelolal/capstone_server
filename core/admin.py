from django.contrib import admin

from .models import Unit, Question, Answer, PeerReview

# Register your models here.
admin.site.register(Unit)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(PeerReview)