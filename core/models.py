from django.db import models
from django.db.models.fields import CharField, TextField, DateField, IntegerField, TimeField

class Unit(models.Model):
  key = IntegerField(primary_key=True)

  def __str__(self):
    return f'Unit {self.key}'

class Question(models.Model):
  title = CharField(max_length=256)
  description = TextField(max_length=16384)
  opens_on = DateField(auto_now=False, auto_now_add=False)
  due_on = DateField(auto_now=False, auto_now_add=False)

  types = ['Test', 'Experiment']
  type = CharField(max_length=64, choices=[(c, c) for c in types])

  def __str__(self):
    return f'Question "{self.title}" opens {self.opens_on} due {self.due_on}'

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
