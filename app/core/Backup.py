# -*- coding: iso-8859-15 -*-
from .job import Job
from pathlib import Path, WindowsPath, PosixPath
from datetime import datetime
import os
import shutil
from .backup_errors import BackUpError


class Backup(object):
    """
    classe che esegue il backup e la gestione delle cartelle di un particolare JOB
    """

    job: Job

    def __init__(self, job: Job):
        self.job = job
        print(f"\nil backup e` stato istanziato: {str(datetime.utcnow())}")
        self.setup_folders()

    # crea i folder  nella cartella di destinazione

    def setup_folders(self):
        # se non c'  la cartella current la crea
        destination = self.job.destination
        if not (destination / "current").exists():
            (destination / "current").mkdir()
            print("creata cartella current")

    # rsync options

    def options(self):
        destination = self.job.destination
        suffix = "{:%Y.%m.%d-%H.%M.%S}".format(datetime.now())
        incremental = destination.joinpath("incremental-" + suffix)
        logfile = destination / "rsync.log' "
        options = (
            "--force --ignore-errors --delete "
            + " --backup --backup-dir='"
            + str(incremental)
            + "' -a -v --perms --chmod=777 "
            + self.inclusions()
            + self.exclusions()
            + " --log-file='"
            + str(logfile)
            + " "
        )
        return options

    def exclusions(self):
        items = self.job.exclude
        option = ""
        for ex in items:
            option = option + " --exclude='" + ex + "' "
        return option

    def inclusions(self):
        items = self.job.include
        option = ""
        for ex in items:
            option = option + " --include='" + ex + "' "
        return option

    def command(self):
        destination = self.job.destination / "current"
        if isinstance(destination, WindowsPath):
            destination = "/" + str(destination.as_posix()).replace(":", "")

        source = self.job.source
        if isinstance(source, WindowsPath):
            source = "/" + str(source.as_posix()).replace(":", "")

        return (
            "rsync "
            + self.options()
            + " '"
            + str(source)
            + "/' '"
            + str(destination)
            + "' "
        )

    def run(self):
        try:
            result = os.system(self.command())
            print("risultato: ", result)
            if result > 0:
                raise Exception("rsync error durante il run del backup")
        except Exception as err:
            raise BackUpError(
                f"Errore nell'esecuzione del comando rsync: \n      il Job non e` stato eseguito \n       Errore: {err}\n\n"
            )
        self.job.set_backup_timedate(type="incremental")

    #############################################
    # cancella gli incremetal più vecchi

    def remove_old_incrementals(self):
        max_copies = self.job.incremental_copies
        folder = self.job.destination

        # recupera la lista di cartelle che contengono nel nome "incremental"
        incrementals = [inc for inc in folder.glob("incremental*") if inc.is_dir()]
        incrementals.sort()
        counter = 0
        while len(incrementals) > max_copies:
            shutil.rmtree(folder / incrementals[0], ignore_errors=True)
            del incrementals[0]
            counter = counter + 1

        return counter

    #############################################
    # cancella i complete più vecchi

    def remove_old_completes(self):
        max_copies = self.job.complete_copies
        folder = self.job.destination

        # recupera la lista di cartelle che contengono nel nome "incremental"
        completes = [
            complete for complete in folder.glob("complete*") if complete.is_dir()
        ]
        completes.sort()
        counter = 0
        while len(completes) > max_copies:
            shutil.rmtree(folder / completes[0], ignore_errors=True)
            del completes[0]
            counter = counter + 1

        return counter

    #############################################
    # genera i completi

    def create_complete(self):
        suffix = "{:%Y.%m.%d-%H.%M.%S}".format(datetime.now())
        folder = self.job.destination

        current = folder.joinpath("current")
        if isinstance(current, WindowsPath):
            current = "/" + str(current.as_posix()).replace(":", "")

        complete = folder.joinpath("complete-" + suffix)
        if isinstance(complete, WindowsPath):
            complete = "/" + str(complete.as_posix()).replace(":", "")

        if self.job.days_since_last_backup() < self.job.complete_frequency:
            return
        else:
            print("creazione nuova copia completa")
            command = (
                "rsync --force --ignore-errors -a -v '"
                + str(current)
                + "/' '"
                + str(complete)
                + "' "
            )
            os.system(command)
            self.job.set_backup_timedate()
