import commands.executeSlashCommands as execCommand
import discord
from discord.ext import commands
from discord.utils import get
import os
from dotenv import load_dotenv

load_dotenv()

# Define your intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True

# Create an instance of a bot
bot = commands.Bot(command_prefix="?", intents=intents)

# Ping command
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong?!')

# Respond to a role mention
@bot.event
async def on_message(message):
    if message.author != bot.user:
    
    # Check if the message mentions a specific role
        bump_role = get(message.guild.roles, name="Bump Remind Ping")
        if bump_role and bump_role.mention in message.content:           
            execCommand.send_command()
            # This is necessary to process commands if you override the on_message event
            await bot.process_commands(message)

# Event listener for when the bot has connected to the server
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')


bot.run(os.getenv('BOT_TOKEN'))
