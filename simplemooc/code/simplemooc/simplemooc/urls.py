# coding: utf-8

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'simplemooc.core.views.home', name='home'),
    url(r'^contato/$', 'simplemooc.core.views.contact', name='contact'),
    url(r'^admin/', include(admin.site.urls)),
)
