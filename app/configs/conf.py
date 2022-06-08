from email.policy import default
from pathlib import Path
from decouple import config
import os
from .email_conf import *

ERROR_LOG = Path(__file__).parent / "../error.log"
LAST_COMPLETE = Path(__file__).parent / "./last-complete"
LAST_INCREMENTAL = Path(__file__).parent / "./last-complete"
SOURCE = Path("/source")
DESTINATION = Path("/destination")
INCREMENTAL = config("INCREMENTAL", default=True, cast=bool)
INCREMENTAL_COPIES = config("INCREMENTAL_COPIES", default=7, cast=int)
COMPLETE_COPIES = config("COMPLETE_COPIES", default=8, cast=int)
COMPLETE_FREQUENCY = config("COMPLETE_FREQUENCY", default=7, cast=int)
LOG = "rsync.log"
EMAIL = config("EMAIL", default="mdognini@eurokemical.it")
EXCLUDE = config("EXCLUDE", cast=lambda v: [s.strip() for s in v.split(",")], default=",")
INCLUDE = config("INCLUDE", cast=lambda v: [s.strip() for s in v.split(",")], default=",")
SCHEDULE_HOUR = config("SCHEDULE_HOUR", default="*")
SCHEDULE_MIN = config("SCHEDULE_MIN", default="*")
