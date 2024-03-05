import time
import translators as ts
import discord

async def MAIN(message, args):
    starttime = time.time()
    messageContent = ' '.join(args)

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

def HELP(PREFIX):
    return {
        "COOLDOWN": 0,
        "MAIN": "Translate text into English.",
        "FORMAT": f"{PREFIX}translate [text]",
        "CHANNEL": 0,
        "USAGE": f"Translate text into English using `{PREFIX}translate [text]`",
        "CATEGORY": "Utility"
    }

PERMS = 0
ALIASES = ["translate"]
REQ = []