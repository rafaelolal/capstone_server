from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.db.models.fields import  IntegerField, BooleanField, CharField, TextField, DateField

class Classroom(models.Model):
  periods = ['A-3/4', 'A-7/8', 'B-3/4', 'B-7/8']
  period = CharField(max_length=6, choices=[(c, c) for c in periods], unique=True)

  def __str__(self):
    return f'{self.period}'

class Unit(models.Model):
  key = ShortUUIDField(length=4, alphabet="012345679", unique=True, primary_key=True)
  signed = BooleanField(null=True)
  classroom = models.ForeignKey(Classroom, related_name="units", on_delete=models.CASCADE, blank=True, null=True)

  types = ['Experimental', 'Control', 'Test']
  type = CharField(max_length=12, choices=[(c, c) for c in types])

  def __str__(self):
    return f'{self.type} {self.key}'

class Question(models.Model):
  title = CharField(max_length=256)
  description = TextField(max_length=16384)
  opens_on = DateField(auto_now=False, auto_now_add=False)
  due_on = DateField(auto_now=False, auto_now_add=False)
  pre_requisite = IntegerField(blank=True, null=True)

  types = ['Test', 'Experiment']
  type = CharField(max_length=10, choices=[(c, c) for c in types])

  def __str__(self):
    return f'{self.pk} "{self.title}" opens {self.opens_on} due {self.due_on}'

class Answer(models.Model):
  unit = models.ForeignKey(Unit, related_name="answers", on_delete=models.CASCADE)
  question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
  
  content = TextField(max_length=16384)
  time_spent = IntegerField(null=True)

  def __str__(self):
    return f'By {self.unit} on "{self.question.title}"'

class PeerReview(models.Model):
  unit = models.ForeignKey(Unit, related_name="peer_reviews", on_delete=models.CASCADE)
  
  content = TextField(max_length=16384)
  submitted_on = DateField(auto_now=False, auto_now_add=False)

  def __str__(self):
    return f'By {self.unit} on {self.submitted_on}'