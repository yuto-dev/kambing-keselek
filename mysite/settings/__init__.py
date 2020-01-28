import os

ENV = os.getenv('MYBLOG_ENV', 'prod')

if ENV == 'dev':
    from .dev import *
elif ENV == 'prod':
    from .production import *
