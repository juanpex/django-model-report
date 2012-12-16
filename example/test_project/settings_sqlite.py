from settings import *

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': PROJECT_ABSOLUTE_DIR + '/model_report.db',                      # Or path to database file if using sqlite3.
     }
 }
