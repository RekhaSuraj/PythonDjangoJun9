from django.shortcuts import render
from myapp1.models import Car


# Create your views here.
def car_list(request):
    car = Car.objects.all()
    return render(request,"list.html", {'car': car})



