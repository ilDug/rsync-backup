import os
from pathlib import Path
from datetime import datetime
from string import Template
from .mail import DagMail, DagMailConfig
from configs.conf import MAIL_CONFIG


class Notifier:
    """
    classe che invia le email di notifica
    """

    def __init__(self):
        self.sender = ""
        self.recipient = ""
        self.header = ""
        self.message = ""

    def to_address(self, address):
        self.recipient = address
        return self

    # def from_address(self, address):
    #     self.sender = address
    #     return self

    def subject(self, text):
        self.header = text
        return self

    def body(self, msg):
        self.message = msg
        return self

    def send(self) -> bool:
        """
        manda la email cn il codice di attivazione edell'account

        @return boolean se la mail è stata invata
        """
        try:
            config = DagMailConfig(**MAIL_CONFIG)
            with DagMail(config) as ms:
                ms.add_receiver(self.recipient)
                ms.messageHTML(self.message, self.subject)
                ms.send()
                return True
        except Exception as e:
            print(str(e))
            return False
