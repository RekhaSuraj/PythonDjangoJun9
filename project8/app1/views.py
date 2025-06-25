from django.shortcuts import render

# Create your views here.


def count_page(request):
    print("current cookies:",request.COOKIES)
    count = int(request.COOKIES.get('count',0))
    count = count + 1

    response = render(request,'count.html',{'count':count})
    response.set_cookie('count',count)
    return response
