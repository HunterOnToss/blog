from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^learn/', 'learn.views.learn'),
                       )