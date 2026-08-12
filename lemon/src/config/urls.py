"""
Root URL configuration.

https://docs.djangoproject.com/en/6.1/topics/http/urls/
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("api.urls")),
    path("", include("lemon.urls")),
    path("api/", include("djoser.urls")),
    path("api/", include("djoser.urls.authtoken")),
]

if settings.DEBUG:
    # django-debug-toolbar is a development-only dependency, so it is wired up
    # only when the local settings enable it.
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
