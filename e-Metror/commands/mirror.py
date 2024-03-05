import time
import discord

async def MAIN(message, args):
    starttime = time.time()
    messageContent = ' '.join(args)

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

def HELP(PREFIX):
    return {
        "COOLDOWN": 0,
        "MAIN": "Mirrors text.",
        "FORMAT": f"{PREFIX}mirror [text]",
        "CHANNEL": 0,
        "USAGE": f"Mirrors text using `{PREFIX}mirror [text]` and gives a time in milliseconds.",
        "CATEGORY": "Utility"
    }

PERMS = 0
ALIASES = ["mirror"]
REQ = []