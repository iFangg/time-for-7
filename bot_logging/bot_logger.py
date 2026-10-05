import os
import logging
import logging.handlers
from datetime import datetime

def init():
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    logging.getLogger('discord.http').setLevel(logging.INFO)

    if not (os.path.isdir('logs')):
        os.mkdir('logs')

    today = datetime.today().strftime('%d-%m-%Y')

    handler = logging.handlers.RotatingFileHandler(
        filename=f'logs/discord-{today}.log',
        encoding='utf-8',
        maxBytes=32 * 1024 * 1024,  # 32 MiB
        backupCount=5,  # Rotate through 5 files
    )
    dt_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger