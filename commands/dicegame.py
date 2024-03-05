import discord
import random as rn
import asyncio

#TODO: Fix embed lookign werid

async def MAIN(message, args):
    number = rn.randrange(1000, 100000)
    factors = []

    for i in range(1, 7):
        if number % i == 0:
            factors.append(i)

    embed = discord.Embed(
        title=f"{message.author.display_name}'s dicegame! 🎲",
        description=f"The number is currently {number}. Use `start` to roll the die!",
        color=discord.Color(0xd6d167)
    )
    embed.set_author(name=message.author.display_name, icon_url=message.author.avatar.url)

    sent_message = await message.channel.send(embed=embed)

    if args and args[0] == 'start':

        roll = rn.randrange(1, 7)

        if roll in factors:
            result_message = f"You won! The number was {number}, and there was a {len(factors)}/6 chance of winning; nice work!"
        else:
            result_message = f"You lost... the number was {number}, and there was a {len(factors)}/6 chance of winning."

        await asyncio.sleep(1)

        embed.description = "The dice has stopped rolling..."
        embed.add_field(
            name=f"The dice rolled a {roll}!",
            value=result_message,
            inline=False
        )

        await sent_message.edit(embed=embed)


def HELP(PREFIX):
    return {
        "COOLDOWN": 0,
        "MAIN": "Play a dicegame.",
        "FORMAT": f"{PREFIX}dicegame (start)",
        "CHANNEL": 0,
        "USAGE": f"A simple dicegame with the bot. `{PREFIX}dicegame` to check the value, and `{PREFIX}dicegame start` to roll!",
        "CATEGORY": "Fun"
    }

PERMS = 0
ALIASES = ["dicegame"]
REQ = []
