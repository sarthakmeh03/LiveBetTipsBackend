from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LiveBetTips.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/user/', include('Api.urls')),
    url(r'^',include('Api.urls')),
    url(r'^api/',include('Api.urls')),
)
