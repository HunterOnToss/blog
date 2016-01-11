from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]

# http://127.0.0.1:8000/snippets.json vs http://127.0.0.1:8000/snippets.api
urlpatterns = format_suffix_patterns(urlpatterns)
