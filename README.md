# rsync-backup
schedule backup with docker container

It run every days (based on cron schedule)

## usage

``` sh
docker run  \
    -v ./src:/source \
    -v ./dest:/destination \
    -e EMAIL=user@example.com \
    rsync-backup
```

Set folders source and destination as volumes into the container.
Or use compose

```yaml
version: "3.9"

services:
  backup:
    image: ildug/rsync-backup:1.0.6
    environment:
      - SCHEDULE_HOUR=* # crontab value for minutes
      - SCHEDULE_MIN=* # crontab value for hours
      - EMAIL=user@example.com
      # INCREMENTAL:true
      # INCREMENTAL_COPIES:7
      # COMPLETE_COPIES:7
      # COMPLETE_FREQUENCY:8
      # EXCLUDE:[node_modules, env]
      # INCLUDE:[...]
    volumes:
      - ./src:/source
      - ./dest:/destination

```


