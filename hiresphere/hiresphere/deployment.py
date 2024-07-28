import os
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]