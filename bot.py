#client = discord.Client(intents=discord.Intents.default())
#id is 1045162043310886962

# bot.py
import os

import discord
from discord import app_commands
from dotenv import load_dotenv
import googletrans

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.all())
prefix = 'm/'

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

'''
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
'''

@client.event
async def on_message(message):
    if(message.content[0:2] != prefix or message.author == client.user):
        return
    
    args = message.content[len(prefix):].split()
    command = args.pop(0).lower()

    if(command == 'mirror'):
        if(args == []):
            await message.channel.send("Send a message for me to mirror!")
        else:
            final = ''
            for i in args:
                final = final + i + " "
            await message.channel.send(final)

client.run(TOKEN)