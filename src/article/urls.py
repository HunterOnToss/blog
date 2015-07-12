from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^1/', 'article.views.basic_one'),
                       url(r'^2/', 'article.views.template_two'),
                       )
