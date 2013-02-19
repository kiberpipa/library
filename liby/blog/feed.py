from django.contrib.syndication.views import Feed

from liby.blog.models import BlogPost


class BlogFeed(Feed):
    title = "KiberKnjiznica RSS"
    description = ""
    link = "/blog/feed/"

    def items(self):
        return BlogPost.objects.all().order_by("-created")[:2]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return u"/blog/%d" % item.id
