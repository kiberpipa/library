from django.shortcuts import render

from liby.books.models import Book, OnlineMaterial

def home(request):
    books = Book.objects.all()
    online = OnlineMaterial.objects.all()
    return render(request, "home.html", {"books": books, "online_books": online})
