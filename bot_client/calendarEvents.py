import logging
from discord.ext import commands
from database import event_queries
from bot_logging import bot_logger

logger: logging = bot_logger.init()

class CalendarEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def events(ctx):
        logger.info("Get events called")
        events = event_queries.getEvents()
        
        # TODO: Format events - maybe put in get events method?
        # events = formatEvents(events)
        await ctx.send("No events found!" if len(events) == 0 else events)