from email.policy import default
from pathlib import Path
from decouple import config
import os
from .email_conf import *

SOURCE = Path("/source")
# SOURCE = Path(__file__).parents[1] / "./source"

DESTINATION = Path("/destination")
# DESTINATION = Path(__file__).parents[1] / "./destination"

ERROR_LOG = DESTINATION / "error.log"
LAST_COMPLETE = DESTINATION / "last-complete"
LAST_INCREMENTAL = DESTINATION / "last-complete"

INCREMENTAL = config("INCREMENTAL", default=True, cast=bool)
INCREMENTAL_COPIES = config("INCREMENTAL_COPIES", default=7, cast=int)
COMPLETE_COPIES = config("COMPLETE_COPIES", default=8, cast=int)
COMPLETE_FREQUENCY = config("COMPLETE_FREQUENCY", default=7, cast=int)
EMAIL = config("EMAIL", default="marco.dognini@dagtech.it")
EXCLUDE = config(
    "EXCLUDE", cast=lambda v: [s.strip() for s in v.split(",")], default=","
)
INCLUDE = config(
    "INCLUDE", cast=lambda v: [s.strip() for s in v.split(",")], default=","
)
SCHEDULE_HOUR = config("SCHEDULE_HOUR", default="*")
SCHEDULE_MIN = config("SCHEDULE_MIN", default="*")
