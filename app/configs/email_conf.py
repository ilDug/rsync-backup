from decouple import config

# EMAIL
###############################
MAIL_CONFIG = {
    "host": config("MAIL_HOST"),
    "port": config("MAIL_PORT", cast=int),
    "user": config("MAIL_USER"),
    "password": config("MAIL_PW"),
}
