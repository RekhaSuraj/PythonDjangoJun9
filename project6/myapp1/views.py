from django.shortcuts import render, redirect
from myapp1.models import Car
from myapp1 import forms


# Create your views here.
def car_list(request):
    car = Car.objects.all()
    return render(request,"list.html", {'car': car})

def carForms(request):
    var1 = forms.Car_form() #Create an empty form
    if request.method == 'POST':
        var2 = forms.Car_form(request.POST)
        if var2.is_valid():
            var2.save() #DB save
            return redirect('/') #redirect to calling page
        else:
            print(var2.errors)

    return render(request,'form.html',{'var1': var1})




