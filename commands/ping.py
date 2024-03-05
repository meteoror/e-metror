import time
import discord

async def MAIN(message):
    starttime = time.time()

    endtime = time.time()
    registertime = (endtime - starttime) * 1000
    embed = discord.Embed(
        title='Pong! 🏓',
        description=f'It took the bot {registertime:.2f} milliseconds to respond.',
        color=discord.Color(0x228b22)
    )
    embed.set_author(name=message.author.display_name, icon_url=message.author.avatar.url)
    await message.channel.send(embed=embed)

def HELP(PREFIX):
    return {
        "COOLDOWN": 0,
        "MAIN": "Pings bot.",
        "FORMAT": f"{PREFIX}ping",
        "CHANNEL": 0,
        "USAGE": f"Pings the bot and returns time in milliseconds using `{PREFIX}ping.`",
        "CATEGORY": "Utility"
    }

PERMS = 0
ALIASES = ["ping"]
REQ = []