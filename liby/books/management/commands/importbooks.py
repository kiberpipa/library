import csv

from django.core.management.base import BaseCommand

from liby.books.models import Book, Author, Genre


class Command(BaseCommand):
    args = '<csv_file>'
    help = 'Imports books from csv'

    def handle(self, *args, **options):
            csv_file = args[0]
            with open(csv_file) as f:
                reader = csv.DictReader(f)

                for line in reader:
                    if not line["Naslov"]:
                        continue
                    book = Book()
                    book.title = line["Naslov"]

                    if line["Letnica"]:
                        book.pub_date = line["Letnica"]
                    if line["ISBN"]:
                        book.isbn = line["ISBN"]

                    book_authors = []

                    raw_authors = line["Avtor"]
                    raw_authors = raw_authors.replace("et al.", "")
                    raw_authors = raw_authors.replace("et al", "")
                    authors = raw_authors.split(";")
                    authors = map(str.strip, authors)

                    book.save()

                    for author_name in authors:
                        try:
                            author = Author.objects.get(name=author_name)
                            if author:
                                print author
                                book_authors.append(author)
                        except:
                            author = Author()
                            author.name = author_name
                            author.save()
                            book_authors.append(author)

                    book.authors.add(*book_authors)
                    book.save()

                    # DRY TODO

                    raw_genres = line["Zanr"]
                    genres = raw_genres.split(",")
                    genres = map(str.strip, genres)
                    if not genres[0]:
                        continue

                    book_genres = []

                    for name in genres:
                        try:
                            genre = Genre.objects.get(genre_name=name)
                            if genre:
                                print genre
                                book_genres.append(genre)
                        except:
                            genre = Genre()
                            genre.genre_name = name
                            genre.save()
                            book_genres.append(genre)

                    book.genres.add(*book_genres)
                    book.save()
