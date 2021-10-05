from pathlib import Path
from configs.conf import SCHEDULE_MIN, SCHEDULE_HOUR
from string import Template


def init_crontab():
    cron = Path('/etc/cron.d/bu-cron')
    default = "$min $hour * * 1-5  /usr/local/bin/python3.9  /app/main.py >> /var/log/cron.log 2>&1"
    template = Template(default)
    tab = template.substitute(min=str(SCHEDULE_MIN), hour=str(SCHEDULE_HOUR))

    with cron.open('w') as c:
        c.write(tab)
        c.write(
            "\n# An empty line is required at the end of this file for a valid cron file.\n")
        c.write("")

    print(cron.read_text())


init_crontab()
