# rsync-backup
schedule backup with docker container

It run daily (based on cron schedule)

## usage

``` sh
docker run  \
    -v ./src:/source \
    -v ./dest:/destination \
    -e EMAIL=user@example.com \
    - e SCHEDULE_MIN=* \
    - e SCHEDULE_HOUR=* \
    rsync-backup
```

Set folders source and destination as volumes into the container.
Or use compose

```yaml
version: "3.9"

services:
  backup:
    # build: ./shop-api
    image: ildug/rsync-backup:1.0.6
    environment:
      - SCHEDULE_HOUR=*
      - SCHEDULE_MIN=*
      - EMAIL=marco.dognini@dagtech.it
      - INCREMENTAL_COPIES:2
      - COMPLETE_COPIES:2
      - COMPLETE_FREQUENCY:2
    #   - INCREMENTAL:True
    #   - EXCLUDE:node_modules,env
    #   - INCLUDE:,
    volumes:
      - ./s:/source
      - ./d:/destination

```


