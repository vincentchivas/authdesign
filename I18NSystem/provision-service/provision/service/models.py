from django.conf import settings
from provision.db import config, desktopdb, presetdb

DB = settings.DOLPHINOP_DB

config(presetdb, **DB)
config(desktopdb, **DB)
