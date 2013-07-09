from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ops.views.home', name='home'),
    # url(r'^ops/', include('ops.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include('admin.urls', namespace = "admin")),
    #url(r'^some/', include(admin.site.urls)),
    #('^site_media/(?P<path>.*)','django.views.static.serve',{'document_root': settings.STATIC_PATH}),
    ('^/(?P<path>.*)','django.views.static.serve',{'document_root': settings.STATIC_PATH}),
    #(r'^img/(?P<path>.*)', 'django.views.static.serve',{'document_root':settings.IMG_DIR}),
    #url(r'^other/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),

)
