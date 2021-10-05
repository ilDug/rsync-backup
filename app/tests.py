# from core.Backup import Backup
# from core.Jobs import Jobs


# jobs = Jobs()
# for job in range(len(jobs)):
#     try:
#         job = jobs.next()
#         bu = Backup(job)
#         print(bu.command())
#     except Exception as err:
#         print(err)


# from core.Notifier import Notifier

# email = Notifier()
# email.from_address("mdognini@eurokemical.it") \
#     .to_address("mdognini@eurokemical.it") \
#     .subject("pyuthon") \
#     .body("il messaggio inviazio") \
#     .send()
from decouple import config
from configs.conf import ERROR_LOG
import os
from configs.conf import INCLUDE


print(INCLUDE)
