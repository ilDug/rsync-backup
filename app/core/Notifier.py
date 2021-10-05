import os
from pathlib import Path
from datetime import datetime


# class Notifier():
#     """
#     classe che invia le email di notifica
#     """

#     def __init__(self):
#         self.sender = ""
#         self.recipient = ""
#         self.header = ""
#         self.message = ""

#     def to_address(self, address):
#         self.recipient = address
#         return self

#     def from_address(self, address):
#         self.sender = address
#         return self

#     def subject(self, text):
#         self.header = text
#         return self

#     def body(self, msg):
#         self.message = msg
#         return self

#     def send(self):
#         temp = Path("src/temp/temp.txt")
#         mail = [
#             f"To: {self.recipient}\n",
#             f"From: {self.sender}\n",
#             f"Subject: {self.header}\n"
#             "\n",
#             self.message + "\n",
#             str(datetime.now())

#         ]
#         with open(temp, 'w') as f:
#                 f.writelines(mail)

#         command = f"sendmail {self.recipient} < {str(temp)}"
#         os.system(command)
