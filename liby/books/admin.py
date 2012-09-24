from liby.books.models import Book, OnlineMaterial, Author, Genre, Publisher
from django.contrib import admin


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


class OnlineInline(admin.TabularInline):
    model = OnlineMaterial
    extra = 0

class MaterialAdmin(admin.ModelAdmin):
    inlines = [
        BookInline,
        OnlineInline,
    ]

admin.site.register(Book)
admin.site.register(OnlineMaterial)
admin.site.register(Author, MaterialAdmin)
admin.site.register(Genre, MaterialAdmin)
admin.site.register(Publisher, MaterialAdmin)
