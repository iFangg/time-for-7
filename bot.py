import os
from dotenv import load_dotenv
from bot_logging import bot_logger
from bot_client.client import init


#### LOGGING ####
logger = bot_logger.init()


### BOT CLIENT INITIALISATION ###
client = init()


### STARTING BOT ###
try:
    load_dotenv()
    bot_token = os.getenv('BOT_TOKEN')
    client.run(bot_token, log_handler=None)
except (ConnectionError, Exception) as e:
    if type(e) == ConnectionError:
        logger.error(f"Could not connect: {e}")
    else:
        logger.error(f"Unknown error: {e}")
