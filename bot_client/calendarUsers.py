import logging
from classes.user import User
from discord.ext import commands
from database import user_queries
from bot_logging import bot_logger

logger: logging = bot_logger.init()

class CalendarUsers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def users(ctx):
        logger.info("Get users called")
        users = user_queries.getUsers()
        
        # TODO: Same formatting task as events
        await ctx.send("No users found!" if len(users) == 0 else users)
    
    async def register(ctx):
        author = ctx.author
        # print(author)
        user = User(author.name)
        user.id = author.id
        
        logger.info(f"Register user called by: {user.name}")
        try:
            user_queries.registerUser(user)
            await ctx.send(f"<@{author.id}>, you have been registered to this server's schedule!")
        except (Exception) as e:
            await ctx.send(f"Error registering, try again\nERROR: {e}")