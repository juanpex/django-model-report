from settings import *

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'model_report',                      # Or path to database file if using sqlite3.
        'USER': 'postgres',                      # Not used with sqlite3.
     }
 }
