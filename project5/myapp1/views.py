from django.shortcuts import render, HttpResponse

# Create your views here.
Books = [
    {'id':1, 'Author':'Lewis Carroll', 'Name':'''Alice's Adventures in Wonderland'''},
    {'id':2, 'Author':'Jane Austen', 'Name':'Pride and Prejudice'},
    {'id':3, 'Author':'Charles Dickens', 'Name':'A Tale of Two Cities'}
    
]


def book_list(request):
    html = ""
    for book in Books:
        html += f'<div><h1>{book['id']}.{book['Author']}</h1><h3>{book['Name']}</h3></div>'

    return HttpResponse(html)


def research(request, id):
    html = ""
    for book in Books:
        if book['id'] == id:
            book_dict = book


    html += f'<h2>{book_dict['Author']}</h2><p>{book_dict['Name']}</p>'

    return HttpResponse(html)
