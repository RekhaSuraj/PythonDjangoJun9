from django.shortcuts import render

# Create your views here.


def count_page(request):
    print("current cookies:",request.COOKIES)
    # Logs all cookies from the current request to the console (for debugging).

    count = int(request.COOKIES.get('count',0))
    # Retrieves the cookie named 'count'. If it doesn’t exist, defaults to 0.

    count = count + 1
    # Increments the count by 1.

    response = render(request,'count.html',{'count':count})
    # Renders the count.html template, passing the current count.

    response.set_cookie('count',count)
    # Sets or updates the 'count' cookie with the new value.

    return response
    #Returns the HTTP response with the updated cookie.

