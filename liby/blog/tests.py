"""
This file contains tests using the unittest module. These will pass
when you run "bin/django test blog".
"""

from django.core.management import call_command
from django.db.models import loading
from django.test import TestCase
from django.test.client import Client
from django.utils.timezone import now
from liby.blog.models import BlogPost


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
            created=now(),
        )

        # add tags to blog post
        self.blogpost.tags.add("tag1", "tag2")

        self.client = Client()

    def tearDown(self):
        """Tear down after each test, flush database and client."""
        call_command('flush', interactive=False, verbosity=0)
        del self.client

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

    def test_blog_archives(self):
        """Test if archives of blogs page returns status code 200."""
        response = self.client.get('/blog/archives/')
        self.assertEqual(response.status_code, 200)

    def test_tag_page(self):
        """Test if tag page returns status code 200."""
        response = self.client.get('/blog/tag/tag1')
        self.assertEqual(response.status_code, 200)

    def test_tag_404(self):
        """Test if nonexistent tag page returns status code 200."""
        response = self.client.get('/blog/tag/notag')
        self.assertEqual(response.status_code, 404)

    def test_feed(self):
        """Test if feed url returns status code 200."""
        response = self.client.get('/blog/feed/')
        self.assertEqual(response.status_code, 200)

    def test_404(self):
        """Test if nonexistent page has status code 404."""
        response = self.client.get('/blog/nopage/')
        self.assertEqual(response.status_code, 404)
