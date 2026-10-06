import discord
import logging
from classes.user import User
from discord.ext import commands
from database import user_queries
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



def init():
    client = MyClient(command_prefix='!', intents=intents)
    
    ### COMMANDS ###
    @client.command()
    async def test(ctx):
        logger.info("Test called")
        await ctx.send("Test called")
    
    @client.command()
    async def events(ctx):
        logger.info("Get events called")
        events = user_queries.getEvents()
        
        # TODO: Format events - maybe put in get events method?
        # events = formatEvents(events)
        await ctx.send("No events found!" if len(events) == 0 else events)
    
    @client.command()
    async def users(ctx):
        logger.info("Get users called")
        users = user_queries.getUsers()
        
        # TODO: Same formatting task as events
        await ctx.send("No users found!" if len(users) == 0 else users)
    
    @client.command()
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

    return client

""" TO THINK:
could have files to load different commands?
- need cogs for these commands

e.g
- base commands file
- event editing commands file
- user config commands file
"""