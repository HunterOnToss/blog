from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^1/', 'article.views.basic_one'),
                       url(r'^2/', 'article.views.template_two'),
                       url(r'^3/', 'article.views.template_three'),
                       url(r'^articles/all/$', 'article.views.articles'),
                       url(r'^articles/get/(?<article_id>)\d+/$', 'article.views.article'),

                       )
