import os
import discord
from dotenv import load_dotenv

from commands import translate, ping, mirror, dicegame, help

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.all())
prefix = 'm/'

@client.event
async def on_ready():
    print('Online! :3')

#TODO: Implement level, perms, and server into MAIN
#TODO: Make new functions!! Dicegame?
@client.event
async def on_message(message):
    if message.content.startswith(prefix) and message.author != client.user:
        args = message.content[len(prefix):].split()
        command = args.pop(0).lower()

        if command == 'translate':
            await translate.MAIN(message, args)
        elif command == 'ping':
            await ping.MAIN(message)
        elif command == 'mirror':
            await mirror.MAIN(message, args)
        elif command == 'dicegame':
            await dicegame.MAIN(message, args)
        elif command == 'help':
            await help.MAIN(message, args)

client.run(TOKEN)