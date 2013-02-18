from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^katalog/$', 'liby.books.views.home', name='katalog'),
    # url(r'^liby/', include('liby.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Grappeli
    url(r'^grappelli/', include('grappelli.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^$', 'flatpage', {'url': '/o-nas/'}, name='home'),
    url(r'^o-nas/$', 'flatpage', {'url': '/o-nas/'}, name='onas'),
    url(r'^skener/$', 'flatpage', {'url': '/skener/'}, name='skener'),
    url(r'^license/$', 'flatpage', {'url': '/license/'}, name='license'),
)
