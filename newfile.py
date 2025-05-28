import discord
from discord.ext import commands
import io
import asyncio

bloomy = "no"

intents = discord.Intents.default()
intents.messages= True
intents.message_content = True
allowed_mentions = discord.AllowedMentions(everyone = True)
bot = commands.Bot(command_prefix='b.', 

@bot.event
async def on_ready():
    print(f"i'm here, as {bot.user.name}.")

@bot.command()
async def hello(ctx):
	"""
    prints Hello World.
   
    """
	await ctx.send('Hello, World!')
	
bot.run(bloomy)