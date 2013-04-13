"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "bin/django test blog".
"""

from django.test import TestCase
from liby.blog.models import BlogPost
from django.core.management import call_command
from django.db.models import loading
from django.test.client import Client

import datetime


class TestStatusCodes(TestCase):

    def setUp(self):
        """Initialize each test."""

        # required for loading data
        loading.cache.loaded = False

        # initialize database from json file
        call_command('loaddata', 'liby/books/fixtures/development.json', verbosity=0)

        # add one blog post
        self.blogpost = BlogPost.objects.create(
            title="Title #1",
            body="Some long text for testing body.",
            created=datetime.date(2000, 1, 1),
        )

        self.client = Client()

    def test_blog(self):
        """Test if main blog page returns status code 200."""
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_blog_at(self):
        """Test if first blog page returns status code 200."""
        response = self.client.get('/blog/1')
        self.assertEqual(response.status_code, 200)

    def test_blog_404(self):
        """Test if n-th blog page returns status code 404."""
        response = self.client.get('/blog/1000')
        self.assertEqual(response.status_code, 404)
