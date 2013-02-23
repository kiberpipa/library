from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView

from django.contrib import admin

from liby.blog.models import BlogPost
from liby.blog.feed import BlogFeed

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^katalog/$', 'liby.books.views.home', name='katalog'),
    # url(r'^liby/', include('liby.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Grappeli admin (static files)
    url(r'^grappelli/', include('grappelli.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Flatpages (static pages)
urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^$', 'flatpage', {'url': '/o-nas/'}, name='home'),
    url(r'^o-nas/$', 'flatpage', {'url': '/o-nas/'}, name='onas'),
    url(r'^skener/$', 'flatpage', {'url': '/skener/'}, name='skener'),
    url(r'^license/$', 'flatpage', {'url': '/license/'}, name='license'),
)

# Blog
urlpatterns += patterns('liby.blog.views',
    url(r'^blog/$', 'blog', name="blog"),
    url(r'^blog/(?P<pk>\d+)$', DetailView.as_view(
                           model=BlogPost,
                           template_name="post.html")),
    url(r'^blog/archives/$', ListView.as_view(
                           queryset=BlogPost.objects.all().order_by("-created"),
                           template_name="archives.html")),
    url(r'^blog/tag/(?P<tag>\w+)$', 'tagpage', name="tagpage"),
    url(r'^blog/feed/$', BlogFeed()),
)
