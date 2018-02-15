"""
Definition of urls for deg_pln.
"""

from django.urls import include, path

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    path('planner/', include('planner.urls')),
    path('admin/', admin.site.urls),
    # Examples:
    # url(r'^$', deg_pln.views.home, name='home'),
    # url(r'^deg_pln/', include('deg_pln.deg_pln.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
