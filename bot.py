import discord
from discord.ext import commands
import io
import asyncio

# This is a base Bot. you're free to change 
# the code, but WITH THIS RULES:
# 1. DO NOT ADD MALICIOUS CODE.
# 2. DO NOT OVERRIDE THE BOT TOKEN,
# UNLESS YOU'RE SELF HOSTING IT. 

tok = "no"

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
	
bot.run(tok)
