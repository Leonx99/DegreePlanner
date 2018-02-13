"""
Definition of urls for deg_pln_mess.
"""

from django.urls import include, path
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    path('new_app/', include('new_app.urls')),
    path('admin/', admin.site.urls),
    # Examples:
    # url(r'^$', deg_pln_mess.views.home, name='home'),
    # url(r'^deg_pln_mess/', include('deg_pln_mess.deg_pln_mess.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
