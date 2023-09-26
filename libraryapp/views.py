from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from libraryapp.models import Book

def vw_books4(request, ):
    return render(request, "book_list4.html", {"books": Book.objects.all()})

def vw_books3(request, ):
    return render(request, "book_list3.html", {"books": Book.objects.all()})

def vw_books2(request, ):
    return render(request, "book_list2.html", {"books": Book.objects.all()})

def vw_books(request, ):
    return render(request, "book_list.html", {"books": Book.objects.all()})

def vw_book4(request, bookid):
    book_lst = Book.objects.filter(bookid=bookid) # [<Book ...>]
    if len(book_lst) == 1:
        book = book_lst[0]
        return render(request, "book3.html", {"book" : book})
    else:
        return HttpResponse('Error!!')

def vw_book3(request, bookid):
    title = "Alice in wonderland"
    author = "Lewis Carroll"
    description = "It is about a girl in a phntasy world"
    return render(request, "book2.html", {"bookid" : bookid, "title" : title, "author" : author, "description" : description})

def vw_book2(request,):
    title = "Alice in wonderland"
    author = "Lewis Carroll"
    description = "It is about a girl in a phntasy world"
    return render(request, "book.html", {"title" : title, "author" : author, "description" : description})

def vw_home(request):
    html = "<html><body>Bienvenue à ma Bibliothèque</body></html>"
    return HttpResponse(html)

def vw_book(request):
    title = "Alice in wonderland"
    author = "Lewis Carroll"
    description = "It is about a girl in a phantasy world"
    my_template = "<html><body><h1>{{ title }}</h1><h2>{{ author }}</h2><p>{{ description }}</p></body></html>"
    html = "<html><body><h1>Alice in wonderland</h1><h2>Lewis Carroll</h2><p>It is about a girl in a phntasy world</p></body></html>"
    return HttpResponse(html)

