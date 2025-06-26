from django.shortcuts import render
from app1.forms import Product


# Create your views here.
def index(request):
    return render(request, 'index.html')


def add_Product(request):
    form = Product()
    response = render(request, 'add.html',{'form':form})
    if request.method == 'POST':
        form = Product(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']

            response.set_cookie(name, quantity, 60)

    return response


def display_cart(request):
    return render(request, 'displaycart.html')
