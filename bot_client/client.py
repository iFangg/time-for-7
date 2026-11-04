import discord
import logging
from discord.ext import commands
from bot_logging import bot_logger
from calendarUsers import CalendarUsers
from calendarEvents import CalendarEvents

intents = discord.Intents.default()
intents.message_content = True
logger: logging = bot_logger.init()

class MyClient(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        await self.process_commands(message)



def init():
    client = MyClient(command_prefix='!', intents=intents)
    
    ### COMMANDS ###
    @client.command()
    async def test(ctx):
        logger.info("Test called")
        await ctx.send("Test called")
    
    # add a how to/help section to this command to show people how to import calendars
    @client.command()
    async def importCalendar():
        pass

    try:
        client.add_cog(CalendarEvents(client))
        logger.info("Loaded events cog")
    except Exception as e:
        logger.error("Unable to add events cog: ", e)
    
    try:
        client.add_cog(CalendarUsers(client))
        logger.info("Loaded users cog")
    except Exception as e:
        logger.error("Unable to add users cog: ", e)

    return client

""" TO THINK:
could have files to load different commands?
- need cogs for these commands

e.g
- base commands file
- event editing commands file
- user config commands file
"""