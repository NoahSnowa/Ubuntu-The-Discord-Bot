
# Ubuntu-The-Discord-Bot - (c) 2020 Noah Snow

import discord
import os
iport asyncio
from config import TOKEN

# Function called on all messages, this will give the bot it's prefix

async def get_prefix(bot, message):
    prefixes = ["apt-get ", "apt "]                             # List of prefixes the bot can use by default
    return commands.when_mentioned_or(*prefixes)(bot, message)  # Returning the list, and checking if the bot was mentioned(known as "pinged")
    
bot = commands.Bot(command_prefix=get_prefix, intents=discord.Intents.all())
bot.remove_command('help')
os.environ["JIKASHU_NO_UNDERSCORE"] = "True"
os.environ["JIKASHU_HIDE"] = "True"

# Loading Cogs

bot.load_extension('jishaku') # JSK is an "eval" substitue - https://pypi.org/project/jishaku/

for cog in os.listdir('cogs'):                   # List the directory "cogs"
    if cog.endswith('.py'):                      # See if the file it finds ends in .py
        bot.load_extension(f"bot.{cogs[:-3]}")   # Load the cog
        
# Main function called when bot is started
  # This will tell you which bot you signed in as
  # And change the status to "Competing in Ubuntu VS. Centos"
  
@bot.event
async def on_ready():

  print(f"Bot online as {bot.user}")
  await asyncio.sleep(5)
  await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(name="Ubuntu VS. Centos", type=5))
  
bot.run(TOKEN) # Run the bot with the Token from the config
