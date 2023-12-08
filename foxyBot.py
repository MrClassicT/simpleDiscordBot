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
    # Ignore messages sent by the bot itself
    if message.author != bot.user:
    
    # Check if the message mentions a specific role
    # Replace 'YOUR_ROLE_ID_HERE' with the actual role ID you want to check for
        bump_role = get(message.guild.roles, name="Bump Remind Ping")
        if bump_role and bump_role.mention in message.content:
            # The bot will type out '!bump' which should be picked up by the bump bot if it's set to listen for commands in messages
            # await message.channel.send('/bump')
            execCommand.send_command()
            # os.system('python3 executeSlashCommands.py')
        
            # This is necessary to process commands if you override the on_message event
            await bot.process_commands(message)


# @bot.command(name='bumpTest')
# async def bump_test_command(ctx):
#     # Call the function to execute the slash command from the command
#     execCommand.send_command()
#     # os.system('python3 executeSlashCommands.py')
#     await ctx.send('Bump test command executed!')




# Event listener for when the bot has connected to the server
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')


bot.run(os.getenv('BOT_TOKEN'))
