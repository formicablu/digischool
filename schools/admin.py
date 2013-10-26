from django.contrib import admin
from olwidget.admin import GeoModelAdmin


# Customize the map
class MyGeoAdmin(GeoModelAdmin):
    options = {
        'layers': ['osm.mapnik'],
        'default_lat': 44,
        'default_lon': 11,
    }

from .models import *

admin.site.register(Year)
admin.site.register(School, MyGeoAdmin)

admin.site.register(MetricType)
admin.site.register(Metric)