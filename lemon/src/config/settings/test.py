"""Settings for the test suite. Selected by pytest in pyproject.toml."""

from .base import *  # noqa: F403

DEBUG = False

# The test runner creates and drops test_<database>, which the application user
# is deliberately not granted. Local and CI databases are disposable, so tests
# connect as the superuser instead of provisioning extra grants.
DATABASES["default"]["USER"] = env("MYSQL_ROOT_USER", default="root")
DATABASES["default"]["PASSWORD"] = env("MYSQL_ROOT_PASSWORD", default="root")

# The default hashers are deliberately slow; tests create users constantly.
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# Throttle counters live in the cache and outlive individual tests, which would
# make results depend on execution order.
REST_FRAMEWORK = {
    **REST_FRAMEWORK,
    "DEFAULT_THROTTLE_RATES": {"anon": None, "user": None},
}
