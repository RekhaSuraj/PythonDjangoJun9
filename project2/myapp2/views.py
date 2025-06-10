from django.shortcuts import render
from django.shortcuts import HttpResponse
import datetime


# Create your views here.
def display_cur_date_time(request):
    cur_time = datetime.datetime.now()
    return HttpResponse(f'Current time is {cur_time}')

