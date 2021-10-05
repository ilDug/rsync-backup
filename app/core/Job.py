# -*- coding: iso-8859-15 -*-
from pathlib import Path
import json
from datetime import datetime
import shutil
from core.backupErrors import JobError, JobWarning, BackUpError
from configs.conf import LAST_COMPLETE, LAST_INCREMENTAL, SOURCE, DESTINATION, INCREMENTAL, INCREMENTAL_COPIES, COMPLETE_COPIES, COMPLETE_FREQUENCY, LOG, EMAIL, EXCLUDE, INCLUDE


class Job():

    date = {"last-complete": None,  "last-incremental": None}

    def __init__(self):
        self.last_complete = LAST_COMPLETE
        self.last_incremental = LAST_INCREMENTAL
        self.source = SOURCE
        self.destination = DESTINATION
        self.incremental = INCREMENTAL
        self.incremental_copies = INCREMENTAL_COPIES
        self.complete_copies = COMPLETE_COPIES
        self.complete_frequency = COMPLETE_FREQUENCY
        self.log = LOG
        self.email = EMAIL
        self.exclude = EXCLUDE
        self.include = INCLUDE

        c = datetime.strptime(
            self.last_complete.read_text(), '%Y-%m-%d %H:%M:%S.%f')
        self.date['last-complete'] = c

        i = datetime.strptime(
            self.last_incremental.read_text(), '%Y-%m-%d %H:%M:%S.%f')
        self.date['last-complete'] = i

        self.check_source_folder()
        self.check_destination_folder()

    #############################################
    # controlla che la directory esista e che non sia vuota.
    # se e` vuota vuol dire che il sever non l'ha montata

    def check_source_folder(self):
        if not self.source.exists():
            raise JobError(
                "la cartella sorgente non esiste.")

        if len([item for item in self.source.iterdir()]) == 0:
            raise JobError(
                "la directory e` vuota,  il backup non verrà eseguito")

    #############################################
    # controlla che la directory esista e che non sia vuota.
    # se e` vuota vuol dire che il sever non l'ha montata

    def check_destination_folder(self):
        if not self.destination.exists():
            raise BackUpError("la cartella di destinazione non esiste.")

    #############################################
    # salva nel file di configurazione l'ultimo backup

    def set_backup_timedate(self, type='complete'):
        last_type = 'last-' + type
        self.date[last_type] = datetime.now().isoformat(' ')

        if last_type == 'last-complete':
            self.last_complete.write_text(str(self.date['last-complete']))

        if last_type == 'last-incremental':
            self.last_incremental.write_text(str(self.date['last-complete']))
    #############################################
    # calcola quanti giorni sono passati dakll'ultimo backup COMPLETO

    def days_since_last_backup(self, type='complete'):
        last_type = 'last-' + type
        now = datetime.now()
        last_backup = self.date[last_type]
        duration = now - last_backup
        return duration.days
