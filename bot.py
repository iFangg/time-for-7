import os
# import sys

import asyncio
from dotenv import load_dotenv
from bot_logging import bot_logger
from bot_client.client import init


#### LOGGING ####
logger = bot_logger.init()

### STARTING BOT ###
try:
    client = asyncio.run(init())
    load_dotenv()
    bot_token = os.getenv('BOT_TOKEN')
    client.run(bot_token, log_handler=None)
except (ConnectionError, Exception) as e:
    print("bot start fail: ", e)
    if type(e) == ConnectionError:
        logger.error(f"Could not connect: {e}")
    else:
        logger.error(f"Unknown error: {e}")
