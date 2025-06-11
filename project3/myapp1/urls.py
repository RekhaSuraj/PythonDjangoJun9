from django.urls import path
from myapp1 import views

urlpatterns = [
    path('greet/', views.greet),
]