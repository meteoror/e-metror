#client = discord.Client(intents=discord.Intents.default())
#id is 1045162043310886962

# bot.py
import os

import discord
from discord import app_commands
from dotenv import load_dotenv
import translators as ts

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
@client.event
async def on_message(message):
    if message.content.startswith(prefix) and message.author != client.user:

        args = message.content[len(prefix):].split()
        command = args.pop(0).lower()
        messageContent = ' '.join(args)  # Joining the arguments into a single string

        if command == 'translate':
            if not messageContent:
                await message.channel.send("Send something for me to translate!")
            else:
                final = ts.translate_text(messageContent, translator='google', to_language='en')
                await message.channel.send(final)
        
        if command == 'ping':
            await message.channel.send("Pong!")
        
        if command == 'mirror':
            if not messageContent:
                await message.channel.send("Send a message for me to mirror!")
            else:
                await message.channel.send(messageContent)

        if command == 'help':
            if args == ['mirror']:
                await message.channel.send("`m/mirror [content]`: The bot mirrors whatever [content] you sent to it!")
            elif args == ['ping']:
                await message.channel.send("`m/ping`: Pings the bot.")
            else:
                await message.channel.send("A general purpose discord bot, coded by @metror. Code is available on github. \nCommands: \n`help`: Help menu. \n`mirror`: Mirrors text. \n`ping`: Pings the bot.")


client.run(TOKEN)
