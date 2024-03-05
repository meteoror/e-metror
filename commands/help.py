import time
import discord
import commands.mirror as mirror
import commands.translate as translate
import commands.ping as ping
import commands.dicegame as dicegame
import commands.mmmm as mmmm

COMMANDS = {
    "mirror": mirror.HELP,
    "translate": translate.HELP,
    "ping": ping.HELP,
    "dicegame": dicegame.HELP,
    "mmmm": mmmm.HELP
}


async def MAIN(message, args):
    if not args:
        embed = discord.Embed(
            title="List of Commands",
            description="Here are the available commands:",
            color=discord.Color(0x228b22)
        )
        for command, help_func in COMMANDS.items():
            help_info = help_func("m/")  # Call the HELP function to get the help information
            embed.add_field(name=help_info["FORMAT"], value=help_info["MAIN"], inline=False)
        await message.channel.send(embed=embed)
    else:
        command = message.content.split()[1]
        if command in COMMANDS:
            help_info = COMMANDS[command]("m/")
            embed = discord.Embed(
                title=f"`m/{command}`",
                description=f"**Usage:** {help_info['FORMAT']}\n**Description:** {help_info['USAGE']}",
                color=discord.Color(0x228b22)
            )
            await message.channel.send(embed=embed)
        else:
            await message.channel.send("Command not found. :(")


def HELP(PREFIX):
    return {
        "COOLDOWN": 0,
        "MAIN": "Help command.",
        "FORMAT": f"{PREFIX}help",
        "CHANNEL": 0,
        "USAGE": f"Gives help information for different parts of the bot.",
        "CATEGORY": "Utility"
    }

PERMS = 0
ALIASES = ["help"]
REQ = []
