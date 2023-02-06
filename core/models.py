from django.db import models
from django.db.models.fields import CharField, TextField, DateField, IntegerField, TimeField

class Unit(models.Model):
  key = IntegerField(primary_key=True)

class Question(models.Model):
  title = CharField(max_length=256)
  description = TextField(max_length=16384)
  open_at = DateField(auto_now=False, auto_now_add=False)
  due_at = DateField(auto_now=False, auto_now_add=False)

  types = ['Pretest', 'Normal', 'Posttest']
  type = CharField(max_length=64, choices=[(c, c) for c in types])

class Answer(models.Model):
  unit = models.ForeignKey(Unit, related_name="answers", on_delete=models.CASCADE)
  question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
  
  content = TextField(max_length=16384)
  time_spent = IntegerField()