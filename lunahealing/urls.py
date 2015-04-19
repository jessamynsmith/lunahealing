from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'lunahealing.apps.pages.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),
)
