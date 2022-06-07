FROM python:3.10-bullseye
LABEL version="1.1.0"
LABEL git="ilDug/rsync-backup"


RUN apt-get update && \
    apt-get install -y cron rsync
#ssmtp

ENV TZ=Europe/Rome

ENV SCHEDULE_HOUR=12
ENV SCHEDULE_MIN=0

ENV INCREMENTAL=True
ENV INCREMENTAL_COPIES=7
ENV COMPLETE_COPIES=8
ENV COMPLETE_FREQUENCY=8
ENV EMAIL=user@example.com
ENV EXCLUDE=node_modules,env
ENV INCLUDE=,

VOLUME /source
VOLUME /destination

WORKDIR /app

COPY ./app/requirements.txt ./requirements.txt
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY ./app .

# # Run the command on container startup
ENTRYPOINT sh /app/init.sh

# CMD ["cron", "&&", "tail", "-f", "/var/log/cron.log"]
# CMD cron && tail -f /var/log/cron.log

# !!!!!!!!!! MODIFICARE AD OGNI CAMBIAMENTO
# docker build  -t ildug/rsync-backup:1.1.0 .
# docker push ildug/rsync-backup:1.1.0
# docker run -i -t -v ./s:/source -v ./s:/destination -e EMAIL=mdognini@eurokemical.it rsync-backup:1.1.0
