from django.shortcuts import render, redirect
from myapp1.models import Car
from myapp1 import forms
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def car_list(request):
    car = Car.objects.all()
    return render(request,"list.html", {'car': car})

@login_required
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

# Update
@login_required
def car_update(request, id):
    f1 = Car.objects.get(id=id)
    if request.method == 'POST':
        f2 = forms.Car_form(request.POST, instance=f1)
        if f2.is_valid():
            f2.save()
            return redirect('/')
        else:
            print(f2.errors)

    return render(request, 'update.html',{'f1': f1})


# Delete
@login_required
def car_delete(request, id):
    var1 = Car.objects.get(id=id)
    var1.delete()

    return redirect('/')


@login_required
def logout(request):
    return render(request, 'logout.html')



