#client = discord.Client(intents=discord.Intents.default())
#id is 1045162043310886962

# bot.py
import os

import discord
from discord import app_commands
from dotenv import load_dotenv
import translators as ts
import time
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.all())
prefix = 'm/'

@client.event
async def on_ready():
    print('Online! :3')

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
    starttime = time.time()
    if message.content.startswith(prefix) and message.author != client.user:

        args = message.content[len(prefix):].split()
        command = args.pop(0).lower()
        messageContent = ' '.join(args)

        if command == 'translate':
            if not messageContent:
                await message.channel.send("Send something for me to translate!")
            else:
                endtime = time.time()
                registertime = (endtime - starttime) * 1000
                final = ts.translate_text(messageContent, translator='google', to_language='en')
                embed = discord.Embed(
                    title=final,
                    description=f'Translated to English in {registertime:.2f} milliseconds.',
                    color=discord.Color(0x228b22)
                )
                embed.set_author(name=message.author.display_name, icon_url=message.author.avatar.url)
                await message.channel.send(embed=embed)
        
        if command == 'ping':
            endtime = time.time()
            registertime = (endtime - starttime) * 1000
            embed = discord.Embed(
                title='Pong! 🏓',
                description=f'It took the bot {registertime:.2f} milliseconds to respond.',
                color=discord.Color(0x228b22)
            )
            embed.set_author(name=message.author.display_name, icon_url=message.author.avatar.url)
            await message.channel.send(embed=embed)
        
        if command == 'mirror':
            if not messageContent:
                await message.channel.send("Send a message for me to mirror!")
            else:
                endtime = time.time()
                registertime = (endtime - starttime) * 1000
                embed = discord.Embed(
                    title=messageContent,
                    description=f'It took the bot {registertime:.2f} milliseconds to respond.',
                    color=discord.Color(0x228b22)
                )
                embed.set_author(name=message.author.display_name, icon_url=message.author.avatar.url)
                await message.channel.send(embed=embed)

        if command == 'help':
            if args == ['mirror']:
                embed = discord.Embed(
                    title='`m/mirror [content]`',
                    description='The bot mirrors whatever [content] you sent to it, with response time.',
                    color=discord.Color(0x228b22)
                )
                await message.channel.send(embed=embed)

            elif args == ['ping']:
                embed = discord.Embed(
                    title='`m/ping`',
                    description='Pings the bot, with response time.',
                    color=discord.Color(0x228b22)
                )
                await message.channel.send(embed=embed)

            elif args == ['translate']:
                embed = discord.Embed(
                    title='`m/translate [content]`',
                    description='Translates [content] into english. Other languages coming soon.',
                    color=discord.Color(0x228b22)
                )
                await message.channel.send(embed=embed)

            else:
                await message.channel.send("A general purpose discord bot, coded by @metror. Code is available on github. \nCommands: \n`help`: Help menu. \n`mirror`: Mirrors text. \n`ping`: Pings the bot. \n`translate`: Translates text.")


client.run(TOKEN)
