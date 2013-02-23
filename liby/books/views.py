from django.shortcuts import render
from django.contrib.flatpages.models import FlatPage

from liby.books.models import Book


def home(request):
    books = Book.objects.all()
    flatpage = FlatPage.objects.get(url="/katalog/")
    return render(request, "home.html", {"books": books, "flatpage": flatpage})
