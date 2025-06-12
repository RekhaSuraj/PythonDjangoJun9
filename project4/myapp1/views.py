from django.shortcuts import render, HttpResponse

"""
What is render()?
In Django, the render() function is part of the django.shortcuts module.
 It is essentially a shortcut method that combines
  several common steps in the view layer of a web application.

   The primary purpose of render() is to take a request, a template,
    and a dictionary of context data and return an HTTP response with the rendered HTML content. 
"""


# Create your views here.
def demo(request):
    return render(request,'demo.html')


def student1(request):
        stu_info = {"Name":'Aparna', 'Age':25, 'Location':'BLR' }
        return render(request,'student.html',stu_info)


def student2(request):
    stu_info = {"Name": 'Vittal', 'Age': 25, 'Location': 'Udupi'}
    return render(request, 'student.html', stu_info)



def student3(request):
    stu_info = {"Name": 'Surendra', 'Age': 25, 'Location': 'Kadapa'}
    return render(request, 'student.html', stu_info)


def index(request):
    return render(request, 'index.html')
