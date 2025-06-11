from django.shortcuts import render, HttpResponse


# Create your views here.
def greet(request):
    return HttpResponse("<h2>Hello Students from myapp1</h2>")