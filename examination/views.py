from django.shortcuts import get_object_or_404, render, redirect

from .models import Person


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


def delete_person(request, pk):
    """r"""
    person = get_object_or_404(Person, pk=pk)
    context = {"person": person}
    if request.method == "POST":
        person.delete()
        return redirect("examination:persons")
    return render(request, "examination/person_delete.html", context)
