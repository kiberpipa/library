from django.db import models


class Author(models.Model):
    """Model representing a book/smt author"""
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
            return self.name


class Genre(models.Model):
    """
    Model representing a gendre.

    For example: drama, IT, horor
    """
    genre_name = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
            return self.genre_name


class Publisher(models.Model):
    """Model representing a publisher"""
    name = models.CharField(max_length=100)

    def __unicode__(self):
            return self.name


class Item(models.Model):
    """Model representing a book or e-material."""
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, related_name="item_authors_set")
    pub_date = models.IntegerField('Year published', blank=True, null=True)
    publisher = models.ForeignKey(Publisher, blank=True, null=True)
    genres = models.ManyToManyField(Genre, related_name="item_genres_set", null=True, blank=True)

    def get_authors(self):
        names = [e.name for e in self.authors.all()]
        return names

    # DRY
    def get_genres(self):
        genres = [e.genre_name for e in self.genres.all()]
        return genres

    def __unicode__(self):
        return "%s - %s" % (self.title, "; ".join(self.get_authors()))


class Book(Item):
    """docstring for P"""
    reading_room_only = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    reserved = models.BooleanField(default=False)
    isbn = models.CharField(max_length=20, blank=True, null=True)

    def clean(self):
        """docstring for clean"""
        from django.core.exceptions import ValidationError
        if not self.isbn:
            return
        self.isbn = self.isbn.replace("-", "").replace(" ", "")
        if not self.isbn.isdigit():
            raise ValidationError("ISBN must be a digit !!!")
        if len(self.isbn) == 10:
            self.isbn = "978" + self.isbn
        if len(self.isbn) != 13:
            raise ValidationError("Lenght is invalid (must be 10 or 13) !!!")
