from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'pages.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),
)
