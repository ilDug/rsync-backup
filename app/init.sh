
# copia le variabili di ambiente nella cartella dell'applicazione 
#in modo che siano raggiungibili da decouple
env > /app/.env

# inizializza l'applicazione (definizione del crontab)
python3  /app/init.py 

# attivava il job del cron
crontab /etc/cron.d/bu-cron 

# esegue cron
cron 

# stampa i risultati
tail -f /var/log/cron.log