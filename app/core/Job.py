# -*- coding: iso-8859-15 -*-
from pathlib import Path
import json
from datetime import datetime
import shutil
from .backup_errors import JobError, JobWarning, BackUpError
from configs.conf import (
    LAST_COMPLETE,
    LAST_INCREMENTAL,
    SOURCE,
    DESTINATION,
    INCREMENTAL,
    INCREMENTAL_COPIES,
    COMPLETE_COPIES,
    COMPLETE_FREQUENCY,
    EMAIL,
    EXCLUDE,
    INCLUDE,
)


class Job:
    """classe che gestisce  le impostazioni generali dell'attività di backup

    - controllo delle cartelle e dei percorsi
    - controllo delle date degli ultimi backup COMPLETI ed INCREMENTAL
    """

    date = {"last-complete": None, "last-incremental": None}

    def __init__(self):
        self.last_complete = LAST_COMPLETE
        self.last_incremental = LAST_INCREMENTAL
        self.source = SOURCE
        self.destination = DESTINATION
        self.incremental = INCREMENTAL
        self.incremental_copies = INCREMENTAL_COPIES
        self.complete_copies = COMPLETE_COPIES
        self.complete_frequency = COMPLETE_FREQUENCY
        self.email = EMAIL
        self.exclude = EXCLUDE
        self.include = INCLUDE

        self.check_source_folder()
        self.check_destination_folder()


        c = datetime.strptime(self.last_complete.read_text(), "%Y-%m-%d %H:%M:%S.%f")
        self.date["last-complete"] = c

        i = datetime.strptime(self.last_incremental.read_text(), "%Y-%m-%d %H:%M:%S.%f")
        self.date["last-complete"] = i


    #############################################
    def check_source_folder(self):
        """
        controlla che la directory esista e che non sia vuota.
        se e` vuota vuol dire che il sever non l'ha montata
        """
        if not self.source.exists():
            print(self.source)
            raise JobError("la cartella sorgente non esiste.")

        if len([item for item in self.source.iterdir()]) == 0:
            raise JobError("la directory e` vuota,  il backup non verrà eseguito")

    #############################################
    def check_destination_folder(self):
        """
        controlla che la directory esista e che non sia vuota.
        se e` vuota vuol dire che il sever non l'ha montata
        """
        if not self.destination.exists():
            raise BackUpError("la cartella di destinazione non esiste.")

        if not self.last_complete.exists():
            self.set_backup_timedate('complete')

        if not self.last_incremental.exists():
            self.set_backup_timedate('incremental')
            

    #############################################
    def set_backup_timedate(self, type="complete"):
        """salva nel file di configurazione l'ultimo backup"""
        last_type = "last-" + type
        self.date[last_type] = datetime.now().isoformat(" ")

        if last_type == "last-complete":
            self.last_complete.write_text(str(self.date["last-complete"]))

        if last_type == "last-incremental":
            self.last_incremental.write_text(str(self.date["last-incremental"]))

    #############################################
    def days_since_last_backup(self, type="complete"):
        """calcola quanti giorni sono passati dakll'ultimo backup COMPLETO"""
        last_type = "last-" + type
        now = datetime.now()
        last_backup = self.date[last_type]
        duration = now - last_backup
        return duration.days
