from django.db import models

class Author(models.Model):
    """Model representing a book/smt author"""
    name = models.CharField(max_length=100)

    def __unicode__(self):
            return self.name

class Genre(models.Model):
    """
    Model representing a gendre.
    
    For example: drama, IT, horor
    """
    gendre_name = models.CharField(max_length=20)

    def __unicode__(self):
            return self.gendre_name


class Publisher(models.Model):
    """Model representing a publisher"""
    name = models.CharField(max_length=100)

    def __unicode__(self):
            return self.name

class Item(models.Model):
    """Model representing a book or e-material."""
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    pub_date = models.IntegerField('Year published', blank=True, null=True)
    publisher = models.ForeignKey(Publisher, blank=True, null=True)
    gendre = models.ForeignKey(Genre, blank=True, null=True)

    def __unicode__(self):
            return "%s - %s" % (self.title, self.author)

class OnlineMaterial(Item):
    """docstring for On"""
    link = models.URLField()


class Book(Item):
    """docstring for P"""
    reading_room_only = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    reserved = models.BooleanField(default=False)
