from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Person, Question, Exam_question
from .forms import PersonForm, NameForm1, QuestionForm


def get_persons(request):
    """r"""
    persons = Person.objects.all()
    context = {"persons": persons}
    return render(request, "examination/persons.html", context)


def get_person(request, pk):
    """r"""
    person = get_object_or_404(Person, id=pk)
    context = {"person": person, "pk": pk}
    return render(request, "examination/person.html", context)


def add_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("examination:persons")
    else:
        form = PersonForm()
    return render(request, "examination/person_add.html", {"form": form})


def add_person_2(request):
    if request.method == "POST":
        form = NameForm1(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            person = Person(
                first_name=data["first_name"],
                last_name=data["last_name"],
                birth_day=data["birth_day"],
            )
            person.save()
        return redirect("examination:persons")
    return render(request, "examination/person_add.html")


def add_person_1(request):
    context = {"person": 1}
    if request.method == "POST":
        data = request.POST
        person = Person(
            first_name=data["your_name"],
            last_name=data["last_name"],
            birth_day=data["birth_day"],
        )
        person.save()
        return redirect("examination:persons")
    return render(request, "examination/person_add_1.html", context)


def delete_person(request, pk):
    """r"""
    person = get_object_or_404(Person, pk=pk)
    context = {"person": person}
    if request.method == "POST":
        person.delete()
        return redirect("examination:persons")
    return render(request, "examination/person_delete.html", context)


def update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
        return redirect("examination:person", pk=pk)
    else:
        form = PersonForm(instance=person)

    context = {"form": form}
    return render(request, "examination/person_update.html", context)


def get_questions(request):
    questions = Question.objects.all()
    context = {"questions": questions}
    return render(request, "examination/questions.html", context)


def delete_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {"question": question}
    if request.method == "POST":
        question.delete()
        return redirect("examination:questions")
    return render(request, "examination/question_delete.html", context)


def add_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("examination:questions")
    else:
        form = QuestionForm()
    return render(request, "examination/question_add.html", {"form": form})


def get_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {"question": question, "pk": pk}
    return render(request, "examination/question.html", context)


def update_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect("examination:questions")
    else:
        form = QuestionForm(instance=question)
    context = {"form": form}
    return render(request, "examination/question_update.html", context)
