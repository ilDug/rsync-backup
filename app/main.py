#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

from pathlib import Path
from core import JobError, JobWarning, BackUpError, Job, Backup
from datetime import datetime
from configs.conf import ERROR_LOG


def main():
    err_msg = None
    try:
        # verifiche iniziali sul job
        job = Job()
        bu = Backup(job)
        bu.run()
        bu.create_complete()
        bu.remove_old_incrementals()
        bu.remove_old_completes()

    except JobError as err:
        print(err, type(err))
        err_msg = str(err)

    except JobWarning as err:
        print(err, type(err))

    except BackUpError as err:
        print(err, type(err))
        err_msg = str(err)

    except Exception as err:
        print(err, type(err))
        err_msg = str(err)

    finally:
        if err_msg is not None:
            print("error trovati: ", err_msg)
            with Path(ERROR_LOG).open("a") as f:
                f.write(str(datetime.now()))
                f.write("   ")
                f.write(err_msg)
                f.write("\n")

            # address = job.email
            # email = Notifier()
            # email.from_address(address) \
            #     .to_address(address) \
            #     .subject("Backup Error " + socket.gethostname()) \
            #     .body(err_msg) \
            #     .send()

    print("Backup terminato con successo")


if __name__ == "__main__":
    main()
    # print("jellyfish")
