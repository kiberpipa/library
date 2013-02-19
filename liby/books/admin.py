from django.contrib import admin

from liby.books.models import Book, Author, Genre, Publisher
from liby.blog.models import BlogPost


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


class MaterialAdmin(admin.ModelAdmin):
    inlines = [
        BookInline,
    ]

admin.site.register(Book)
admin.site.register(Author, MaterialAdmin)
admin.site.register(Genre, MaterialAdmin)
admin.site.register(Publisher, MaterialAdmin)
admin.site.register(BlogPost)
