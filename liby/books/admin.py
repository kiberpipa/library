from django.contrib import admin

from liby.books.models import Book, Author, Genre, Publisher
from liby.blog.models import BlogPost


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


class BookAdmin(admin.ModelAdmin):
    inlines = [
        BookInline,
    ]


class AuthorsInline(admin.TabularInline):
    model = Book.authors.through
    extra = 0


class AuthorsAdmin(admin.ModelAdmin):
    inlines = [
        AuthorsInline,
    ]


class GenresInline(admin.TabularInline):
    model = Book.genres.through
    extra = 0


class GenresAdmin(admin.ModelAdmin):
    inlines = [
        GenresInline,
    ]

admin.site.register(Book)
admin.site.register(Author, AuthorsAdmin)
admin.site.register(Genre, GenresAdmin)
admin.site.register(Publisher, BookAdmin)
admin.site.register(BlogPost)
