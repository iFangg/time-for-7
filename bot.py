# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
from bot_logging import bot_logger
import os
from dotenv import load_dotenv
from database import db_conn


#### LOGGING ####
logger = bot_logger.init()

### CLIENT ###
class MyClient(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        await self.process_commands(message)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(command_prefix='!', intents=intents)

### COMMANDS ###
@client.command()
async def test(ctx):
    bot_logger.info("Test called")
    await ctx.send("Test called")

# client.add_command(testCommand)

### RUNNING BOT ###
load_dotenv()
db_conn.db_connect(logger)

bot_token = os.getenv('BOT_TOKEN')
client.run(bot_token, log_handler=None)
