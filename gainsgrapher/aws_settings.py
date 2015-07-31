import os
from sys import stderr

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT'],
    }
}

# Django settings for project_management project.
DEBUG = os.environ.get("DEBUG", False)
TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT = os.path.abspath(os.path.dirname(__name__))

ALLOWED_HOSTS = ['localhost', ]

STATIC_ROOT = PROJECT_ROOT + '/static'

# Compressor Settings
COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)
COMPRESS_URL = 'https://.s3.amazonaws.com/'
COMPRESS_STORAGE = 'core.storage.CachedS3BotoStorage'  # 'storages.backends.s3boto.S3BotoStorage'
COMPRESS_ROOT = STATIC_ROOT

STATIC_URL = COMPRESS_URL
STATICFILES_STORAGE = COMPRESS_STORAGE

DEFAULT_FILE_STORAGE = COMPRESS_STORAGE

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = ''

SECRET_KEY = 'pl*^#9hu0yd1=kx!lo!jprlqebzc*f$rx)2ws+g7z(r8-oq80a'

import requests

EC2_PRIVATE_IP = None
try:
    EC2_PRIVATE_IP = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4', timeout=0.01).text
except requests.exceptions.RequestException:
    pass

if EC2_PRIVATE_IP:
    ALLOWED_HOSTS.append(EC2_PRIVATE_IP)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'stderr': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'stream': stderr,
        },
        'slack-error': {
            'level': 'ERROR',
            'class': 'core.loggers.SlackLogHandler',
            'logging_url': 'https://hooks.slack.com/services/<WEBHOOK>/<URL>',
            'stack_trace': True
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'slack-error', ],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security.DisallowedHost': {
            'handlers': ['stderr'],
            'level': 'CRITICAL',
            'propagate': False,
        },
    },

}
