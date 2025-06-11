from django.shortcuts import render, HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse("<h2>This is from myapp2</h2>")
