from django.db import models
from django.db.models.fields import CharField, TextField, DateField, IntegerField, TimeField

class Unit(models.Model):
  key = IntegerField(primary_key=True)

class Question(models.Model):
  title = CharField(max_length=256)
  description = TextField(max_length=5096)
  open_at = DateField(auto_now=False, auto_now_add=False)
  due_at = DateField(auto_now=False, auto_now_add=False)

  types = ['Pretest', 'Normal', 'Posttest']
  tuple_types = [(c, c) for c in types]
  type = CharField(max_length=64, choices=tuple_types)


class Answer(models.Model):
  unit_id = models.ForeignKey(Unit, verbose_name=("unit"), on_delete=models.CASCADE)
  question_id = models.ForeignKey(Question, verbose_name=("question"), on_delete=models.CASCADE)
  
  response = TextField(max_length=5096)
  time_spent = TimeField(auto_now=False, auto_now_add=False)