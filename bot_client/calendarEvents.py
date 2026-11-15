import logging
from discord.ext import commands
from database import event_queries
from bot_logging import bot_logger
from util import calendar_import as calImp

logger: logging = bot_logger.init()

class CalendarEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def events(self, ctx: commands.Context):
        logger.info("Get events called")
        events = event_queries.getEvents()
        
        # TODO: Format events - maybe put in get events method?
        # events = formatEvents(events)
        await ctx.send("No events found!" if len(events) == 0 else events)
    
    @commands.command()
    async def addCalendar(self, ctx: commands.Context, arg):
        pass
        
    # add a how to/help section to this command to show people how to import calendars
    @commands.command()
    async def importCalendar(self, ctx: commands.Context, arg):
        if not arg:
            print("Empty calendar url")
        
        print(f"command user input: ", arg)
        print(f"server: {ctx.guild} - {ctx.guild.id}")
        logger.info("Import calendar called")
        
        # events = calImp.grabCalendar(arg)
        # for event in events:
        #     event.
        #     event_queries.upsertEvent(event)
        