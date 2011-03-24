from django.conf.urls.defaults import *
from mysite.views import contact, search_form

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',#('^hello/$', hello),('^time/$', current_datetime),
    # Example:
   # (r'^mysite/', include('mysite.foo.urls')),
    (r'^admin/', include(admin.site.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^search/$', search_form),
     #(r'^search/$', search),
     (r'^contact/$', contact),
     (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/media/SOUMYA/Django_proj/djcode/mysite/static/', 'show_indexes': True}),
)
