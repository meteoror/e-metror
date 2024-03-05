import time
import discord

#TODO: Finish coding

async def MAIN(message, args):
    starttime = time.time()
    messageContent = ' '.join(args)

    if not messageContent:
        await message.author.send("Send a message for me to mirror!")
    else:
        endtime = time.time()
        registertime = (endtime - starttime) * 1000
        embed = discord.Embed(
            title=messageContent,
            description=f'It took the bot {registertime:.2f} milliseconds to respond.',
            color=discord.Color(0x228b22)
        )
        embed.set_author(name=message.author.display_name, icon_url=message.author.avatar.url)
        await message.author.send(embed=embed)

def HELP(PREFIX):
    return {
        "COOLDOWN": 0,
        "MAIN": "Writing game",
        "FORMAT": f"{PREFIX}write",
        "CHANNEL": 0,
        "USAGE": f"A collaborative writing game for servers, similar to a mini-mini TWOW.",
        "CATEGORY": "Fun"
    }

PERMS = 0
ALIASES = ["write"]
REQ = []