FROM python:3.9-buster
LABEL version="1.0.6"
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

# Add crontab file in the cron directory
ADD ./backup-crontab /etc/cron.d/bu-cron

# Give execution rights on the cron job
RUN chmod 0777 /etc/cron.d/bu-cron

# Apply cron job
RUN crontab /etc/cron.d/bu-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
ENTRYPOINT sh /app/init.sh



# !!!!!!!!!! MODIFICARE AD OGNI CAMBIAMENTO
# docker build  -t ildug/rsync-backup:1.0.6 .
# docker push ildug/rsync-backup:1.0.6
#docker run -i -t -v ./src:/source -v ./dest:/destination -e EMAIL=mdognini@eurokemical.it rsync-backup:1.0.6
