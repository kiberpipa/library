# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from liby.blog.models import BlogPost


def tagpage(request, tag):
    posts = BlogPost.objects.filter(tags__name=tag)
    return render_to_response("tagpage.html", {"posts": posts, "tag": tag}, RequestContext(request))
