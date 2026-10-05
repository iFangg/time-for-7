import discord
import logging
from database import db_queries
from discord.ext import commands
from bot_logging import bot_logger

intents = discord.Intents.default()
intents.message_content = True
logger: logging = bot_logger.init()

class MyClient(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        await self.process_commands(message)



def closeConnection(cur):
    cur.close()

def init():
    client = MyClient(command_prefix='!', intents=intents)
    
    ### COMMANDS ###
    @client.command()
    async def test(ctx):
        logger.info("Test called")
        await ctx.send("Test called")
    
    # @client.after_invoke(closeConnection)
    @client.command()
    async def events(ctx):
        logger.info("Get events called")
        events = db_queries.getEvents()
        
        # TODO: Format events - maybe put in get events method?
        # events = formatEvents(events)
        await ctx.send("No events found!" if len(events) == 0 else events)
    
    @client.command()
    async def users(ctx):
        logger.info("Get users called")
        users = db_queries.getUsers()
        
        # TODO: Same formatting task as events
        await ctx.send("No users found!" if len(users) == 0 else users)

    return client

""" TO THINK:
could have files to load different commands?
- need cogs for these commands

e.g
- base commands file
- event editing commands file
- user config commands file
"""