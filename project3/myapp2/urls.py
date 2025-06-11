from django.urls import path
from myapp2 import views

urlpatterns = [
    path("hello/",views.hello)
]