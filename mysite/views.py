from django.shortcuts import get_object_or_404, render, HttpResponseRedirect

def home(request):
    return render(request, "home/home.html")
