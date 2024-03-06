import discord
import json

class Response:
    def __init__(self, author='', content='', votes=0):
        self.author = author
        self.content = content
        self.votes = votes

class Game:
    def __init__(self, started=False, host='', hostid=0, story='', players=0, plist=[], responses=[]):
        self.started = started
        self.host = host
        self.hostid = hostid
        self.story = story
        self.players = players
        self.plist = plist
        self.responses = responses

async def save_game_state(current_game):
    with open("game_state.json", "w") as file:
        json.dump(current_game.__dict__, file)

async def load_game_state():
    try:
        with open("game_state.json", "r") as file:
            data = json.load(file)
            current_game = Game()
            current_game.__dict__.update(data)
            return current_game
    except FileNotFoundError:
        return None

import os

async def end_game():
    try:
        os.remove("game_state.json")
        return True
    except FileNotFoundError:
        return False

async def send_dm(user_id, message_content, client):
    try:
        user = await client.fetch_user(user_id)
        await user.send(message_content)
    except discord.errors.HTTPException as e:
        print(f"Failed to send DM to user with ID {user_id}: {e}")

async def MAIN(message, args, client):
    messender = message.author.display_name
    messenderid = message.author.id
    messageContent = ' '.join(args[1:])
    current = await load_game_state()
    game = []
    command = args[0].lower()

    if command == 'start':
        if current is None or not current.started:
            await message.author.send("You are now hosting the game.")
            current = Game(True, messender, messenderid, '', 0, [], [])
            await save_game_state(current)
        else:
            await message.channel.send(f"{current.host} is already hosting a Write or Die game!")

    if command == 'join':
        if current is not None:
            current.players += 1
            current.plist.append(messender)
            await save_game_state(current)
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

        if isplaying:
            if not messageContent:
                await message.author.send("Please enter a response!")
            else:
                playerResponse = Response(messender, messageContent, 0)
                current.responses.append([playerResponse.author, playerResponse.content, playerResponse.votes])
                await message.author.send(f"Your response has been logged as `{messageContent}`.")
                # Send a message to the host
                host_id = current.hostid  # Replace this with the actual attribute that stores the host's ID
                await send_dm(host_id, f"{messender} has responded to the game: `{messageContent}`", client)

    if command == 'end':
        success = await end_game()
        if success:
            await message.channel.send("The game has ended.")
        else:
            await message.channel.send("No game currently active.")

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
