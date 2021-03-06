from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^basicview/', include('article.urls')),
    url(r'^auth/', include('login_sys.urls')),
    url(r'^', include('article.urls')),
    url(r'^', include('learn.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^', include('snippets.urls')),
    url(r'^bank/', include('hunter_bank.urls', namespace="bank")),
)

urlpatterns += staticfiles_urlpatterns() + static(
settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
