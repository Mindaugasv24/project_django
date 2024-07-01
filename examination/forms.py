from django import forms
from .models import Person, Question


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"


class NameForm1(forms.Form):
    first_name = forms.CharField(label="your_name", max_length=105)
    last_name = forms.CharField(label="your_last_name", max_length=100)
    birth_day = forms.DateField(label="your_birth_day")


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"


class QuestionForm1(forms.Form):
    complexity_level = forms.CharField(label="complexity_level", max_length=100)
    question = forms.CharField(label="question", max_length=100)
