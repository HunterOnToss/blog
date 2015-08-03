from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^login/', 'login_sys.views.login'),
                       url(r'^logout/', 'login_sys.views.logout'),
                       url(r'^register/', 'login_sys.views.register'),
                       )
