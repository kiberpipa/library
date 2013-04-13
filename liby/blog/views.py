# Create your views here.
from django.contrib.flatpages.models import FlatPage
from django.http import Http404
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from liby.blog.models import BlogPost


def blog(request):
    """docstring for blog"""
    flatpage = FlatPage.objects.get(url="/blog/")
    queryset = BlogPost.objects.all().order_by("-created")[:5]
    tags = BlogPost.objects.values('tags__name').distinct()
    tags = [tag["tags__name"] for tag in tags]
    return render(request, "blog.html", {"queryset": queryset, 'tags': tags, "flatpage": flatpage})


def tagpage(request, tag):
    posts = BlogPost.objects.filter(tags__name=tag)

    # raise 404 if there is no posts for this tag
    if not posts:
        raise Http404

    return render_to_response("tagpage.html", {"posts": posts, "tag": tag}, RequestContext(request))
