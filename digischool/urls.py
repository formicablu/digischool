from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'schools.views.index', name='home'),
    # url(r'^digischool/', include('digischool.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^map$', 'schools.views.map'),
	url(r'^map.meta$', 'schools.views.mapping'),
	url(r'^map.geojson$', 'schools.views.geoj'),
	url(r'^search', 'schools.views.search'),
	url(r'^timeline', 'legal.views.timeline'),
	url(r'^evaluate', 'schools.views.evaluate'),


)
