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
    url(r'^basic/$', basic),                   # - The basic template page
    url(r'^data/$', data_hora),                # - First test page
    url(r'^clients/$', clients),               # + Mostra els clients per despres poder fer una comanda
    url(r'^contact/$', contact),               # Pagina de contacte
    url(r'^thanks/$', thanks),                 # -Apreciacion page, not important
    url(r'^comanda/$', comanda),               # 
    url(r'^productes/$', producte),            # 
    url(r'^detall_comanda/$', detall_comanda), # 
    url(r'^search-form/$', search_form),       # - Just a test page form
    url(r'^search/$', search),                 # - The test page itself
    url(r'^prova/$', prova),                   # - Another test page
    url(r'^fes_comanda/$', fes_comanda),       # + Enllasat amb el url clients
    url(r'^veure_comanda/$', veure_comanda),   # + Pagina destinada per veure les comandes



)

