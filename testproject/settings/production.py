import os
from django.conf import settings

DEBUG = False
TEMPLATE_DEBUG = True
DATABASES = settings.DATABASES


# Update database configuration with $DATABASE_URL.
import dj_database_url


# import os
# import psycopg2
# import urllib.parse as up

# up.uses_netloc.append("postgres")
# url = up.urlparse(os.environ["DATABASE_URL"])

# conn = psycopg2.connect(
#     database=url.path[1:],
#     user=url.username,
#     password=url.password,
#     host=url.hostname,
#     port=url.port
# )


db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
# DATABASES['default'] = dj_database_url.config(conn_max_age=500)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static_root')
# # STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
# STATIC_URL = '/static/'

# # Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#     os.path.join(PROJECT_ROOT, 'static'),
# )

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'