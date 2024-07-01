from datetime import datetime

from django.db import models


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

    COMPLEXITY_LEVEL = {
        "1": "Easy",
        "2": "Medium",
        "3": "Hard",
    }
    question = models.CharField(max_length=200)
    complexity = models.CharField(max_length=100, choices=COMPLEXITY_LEVEL)

    def __str__(self):
        return f"{self.question} {self.complexity}"


class Examquestion(BaseModel):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.exam} {self.question}"


class Answer(BaseModel):
    answer = models.CharField(max_length=100)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.answer} {self.correct} {self.question}"


class Result(BaseModel):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person} {self.exam} {self.answer}"
