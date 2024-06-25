from datetime import datetime

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Person(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    birth_day = models.DateField(default=datetime(year=2000, month=1, day=1))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


topic = ["Animal", "KET"]


class Exam(BaseModel):
    subject = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.subject} {self.topic}"


class Question(BaseModel):
    """r"""

    question = models.CharField(max_length=200)
    dificulty = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.question} {self.dificulty}"


class Exam_question(BaseModel):
    exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.exam_id} {self.question_id}"


# class Answer(BaseModel):
#     answer = models.CharField(max_length=100)
#     correct = models.BooleanField(default=False)
#     question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.answer}'


# class Result(BaseModel):
#     person_answer = models.CharField(max_length=200)
#     person_id = models.ForeignKey(Question, on_delete=models.CASCADE)
#     exam_id = models.ForeignKey(Question, on_delete=models.CASCADE)
#     question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.person_answer}'
