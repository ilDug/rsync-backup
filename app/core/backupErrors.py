class JobError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class JobWarning(Warning):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class BackUpError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
