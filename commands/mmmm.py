import discord

async def encode(text):
    encoding = {
        'A': 'А', 'B': 'В', 'C': 'С', 'D': 'Д', 'E': 'Е',
        'F': 'Ф', 'G': 'Г', 'H': 'Н', 'I': 'И', 'J': 'DЗ',
        'K': 'К', 'L': 'Л', 'M': 'М', 'N': 'Њ', 'O': 'О',
        'P': 'Р', 'Q': 'Ч', 'R': 'Р', 'S': 'Ѕ', 'T': 'Т',
        'U': 'У', 'V': 'В', 'W': 'Ш', 'X': 'Х', 'Y': 'У',
        'Z': 'З',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D',
        'Е': 'E', 'Ж': 'Ж', 'З': 'Z', 'И': 'И', 'Ј': 'ДЗ',
        'К': 'K', 'Л': 'Л', 'М': 'M', 'Н': 'H', 'О': 'O',
        'П': 'П', 'Р': 'P', 'С': 'C', 'Т': 'T', 'У': 'U',
        'Ф': 'F', 'Х': 'X', 'Ц': 'Ц', 'Ч': 'Q', 'Ш': 'W',
        'Џ': 'Џ', 'Ш': 'W', 'Њ': 'N', 'Љ': 'Л', 'Ђ': 'Ђ',
        'Ћ': 'C', 'Ѕ': 'S', 'Џ': 'J', 'Ц': 'Ц',
    }
    encoded_text = ''
    for c in text:
        if c.upper() in encoding:
            if c.isupper():
                encoded_text += encoding[c.upper()]
            else:
                encoded_text += encoding[c.upper()].lower()
        else:
            encoded_text += c
    return encoded_text

async def decode(text):
    decoding = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D',
        'Е': 'E', 'Ж': 'Ж', 'З': 'Z', 'И': 'И', 'Ј': 'J',
        'К': 'K', 'Л': 'Л', 'М': 'M', 'Н': 'H', 'О': 'O',
        'П': 'П', 'Р': 'P', 'С': 'S', 'Т': 'T', 'У': 'Y',
        'Ф': 'F', 'Х': 'X', 'Ц': 'Ц', 'Ч': 'Q', 'Ш': 'W',
        'Џ': 'J', 'Ѕ': 'S',
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
        'е': 'e', 'ж': 'ж', 'з': 'z', 'и': 'и', 'ј': 'j',
        'к': 'k', 'л': 'л', 'м': 'm', 'н': 'h', 'о': 'o',
        'п': 'п', 'р': 'r', 'с': 's', 'т': 't', 'у': 'у',
        'ф': 'f', 'х': 'x', 'ц': 'ц', 'ч': 'q', 'ш': 'w',
        'џ': 'џ', 'љ': 'л', 'ђ': 'ђ', 'ћ': 'c', 'ѕ': 's',
    }
    decoded_text = ''
    for c in text:
        if c in decoding:
            decoded_text += decoding[c]
        else:
            decoded_text += c
    return decoded_text

async def MAIN(message, args):
    if len(args) < 2:
        await message.channel.send("Please provide both 'encode' or 'decode' and the text to encrypt or decrypt.")
        return
    
    operation = args[0].lower()
    text = ' '.join(args[1:])
    
    if operation == 'encode':
        result = await encode(text)
    elif operation == 'decode':
        result = await decode(text)
    else:
        await message.channel.send("Invalid operation. Please choose 'encode' or 'decode'.")
        return
    
    await message.channel.send(result)

def HELP(PREFIX):
    return {
        "COOLDOWN": 0,
        "MAIN": "Different cryptography fun-ctions.",
        "FORMAT": f"{PREFIX}mmmm (args) [content]",
        "CHANNEL": 0,
        "USAGE": "Metror's Marvelous Mechanical Magi-codes hosts a variety of different cryptography games. Use (encode|decode) to get text in a secret language!",
        "CATEGORY": "Fun"
    }

PERMS = 0
ALIASES = ["mmmm"]
REQ = []
