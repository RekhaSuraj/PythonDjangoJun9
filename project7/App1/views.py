from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from App1.models import Product

# from django.views import View
# This imports the base class for Class-Based Views (CBVs).
# You can use it to create your own custom views by subclassing View.
# You need to define your own HTTP methods like get(), post(), etc.

# from django.views.generic import ListView
# ListView is a pre-built generic class-based view for displaying a list of objects from a model.
# It handles querying the database, rendering the template, and passing context — all with very little code.


class Greetings(View):

    def get(self,request):
        return HttpResponse('<h2>Welcome to class based views</h2>')


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    # fields = 'Pname'
    fields = '__all__'


class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('pro1')
