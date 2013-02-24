from django.shortcuts import render
from django.contrib.flatpages.models import FlatPage

from liby.books.models import Book


def books(request):
    books = Book.objects.all()
    flatpage = FlatPage.objects.get(url="/katalog/")
    return render(request, "books.html", {"books": books, "flatpage": flatpage})
