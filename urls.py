from django.conf.urls.defaults import *
import dbindexer
from django.contrib import admin
from app1.views import *


handler500 = 'djangotoolbox.errorviews.server_error'

# django admin
admin.autodiscover()

# search for dbindexes.py in all INSTALLED_APPS and load them
dbindexer.autodiscover()

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
    ('^admin/', include(admin.site.urls)),
    url(r'^basic/$', basic),
    url(r'^data/$', data_hora),
    url(r'^clients/$', clients),
    url(r'^contact/$', contact),
    url(r'^thanks/$', thanks),
    url(r'^comanda/$', comanda),
    url(r'^productes/$', producte),
    url(r'^detall_comanda/$', detall_comanda),
)

