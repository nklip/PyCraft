"""Settings for local development. The default for manage.py and run.sh."""

from .base import *  # noqa: F403

DEBUG = env.bool("DJANGO_DEBUG", default=True)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["127.0.0.1", "localhost"])


# django-debug-toolbar
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
#
# A development-only dependency, so it is installed and configured only here.

INSTALLED_APPS += ["debug_toolbar"]

# The toolbar wraps the response, so its middleware runs as early as possible.
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

INTERNAL_IPS = ["127.0.0.1"]
