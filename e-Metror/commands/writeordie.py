import time
import discord
import json

#TODO: Bug test. You need to make the game a global variable!!!

class Response:
    def __init__(self, author, content, votes):
        author = ''
        content = ''
        votes = 0

class Game:
    def __init__(self, started, host, story, players, plist, responses):
        started = False
        host = ''
        story = ''
        players = 0
        plist = []
        responses = []

# Function to save the game state to a file
async def save_game_state(current_game):
    with open("game_state.json", "w") as file:
        json.dump(current_game.__dict__, file)

# Function to load the game state from a file
async def load_game_state():
    try:
        with open("game_state.json", "r") as file:
            data = json.load(file)
            current_game = Game()
            current_game.__dict__.update(data)
            return current_game
    except FileNotFoundError:
        return None

async def MAIN(message, args):
    messender = message.author.display_name
    messageContent = ' '.join(args[1:])
    current = load_game_state()  # Load the game state from the file
    game = []
    command = args[0].lower()

    if command == 'start':
        if current is None or not current.started:
            current = Game()
            current.started = True
            current.host = messender
            save_game_state(current)  # Save the game state after modification
        else:
            await message.channel.send(f"{current.host} is already hosting a Write or Die game!")

    if command == 'join':
        if current is not None:
            current.players += 1
            current.plist.append(messender)
            save_game_state(current)  # Save the game state after modification
            await message.channel.send(f"{messender} has joined the Write or Die! There are now {current.players} participants.")
        else:
            await message.channel.send("No game currently active. Start a game first.")

    if command == 'respond':
        isplaying = False
        if current is not None:
            for i in current.plist:
                if i == messender:
                    isplaying = True

            if not current.started:
                await message.author.send("You can only respond if a game has started!")
            elif not isplaying:
                await message.author.send("You can only respond if you are playing!")
        else:
            await message.channel.send("No game currently active. Start a game first.")


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