# inizializza l'applicazione (definizione del crontab)
# python3  /app/init.py 

touch /var/log/cron.log
touch /etc/cron.d/back-up-cron
chmod 0777 /etc/cron.d/back-up-cron

echo "$SCHEDULE_MIN $SCHEDULE_HOUR * * 1-6 /usr/local/bin/python3.10  /app/main.py >> /var/log/cron.log 2>&1" > /etc/cron.d/back-up-cron

echo "# An empty line is required at the end of this file for a valid cron file." >> /etc/cron.d/back-up-cron 

echo "" >> /etc/cron.d/back-up-cron

# attivava il job del cron
crontab /etc/cron.d/back-up-cron

# esegue cron
cron 

# stampa i risultati
tail -f /var/log/cron.log