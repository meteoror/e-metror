import discord
import json
import os
import random

class Response:
    def __init__(self, author='', content='', votes=0):
        self.author = author
        self.content = content
        self.votes = votes

class Game:
    def __init__(self, started=False, host='', hostid=0, story='', players=0, plist=[], playerid=[], responses=[], responding = False, voting = False):
        self.started = started
        self.host = host
        self.hostid = hostid
        self.story = story
        self.players = players
        self.plist = plist
        self.playerid = playerid
        self.responses = responses
        self.responding = False
        self.voting = False

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

async def number_to_letter(num):
    return chr(num + 64)

async def generateBoard(responses, key):
    random.shuffle(responses)
    board = '# Voting \n\n'
    responseNumber = 1
    boardkey = []
    for i in responses:
        letter = await number_to_letter(responseNumber)
        response = i[1]
        board = board + (f"{letter}: {response}\n")
        boardkey.append([letter, responseNumber, response])
        responseNumber += 1
    board = board + "\n Vote for your favorite with `m/write vote`!"
    if key:
        return boardkey
    else:
        return board
    


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
            current = Game(True, messender, messenderid, '', 0, [], [], [], False, False)
            await save_game_state(current)
        else:
            await message.channel.send(f"{current.host} is already hosting a Write or Die game!")

    if command == 'join':
        alreadyJoined = False
        for i in current.plist:
            if i == messender:
                alreadyJoined = True
        
        if alreadyJoined == False:
            if current is not None:
                current.players += 1
                current.plist.append(messender)
                current.playerid.append(messenderid)
                await save_game_state(current)
                await message.channel.send(f"{messender} has joined the Write or Die! There are now {current.players} participants.")
            else:
                await message.channel.send("No game currently active. Start a game first.")
        else:
            await message.channel.send("You have already joined the game!")

    if command == 'openresponding':
        if current is not None and messenderid == current.hostid and current.responding is False:
            current.responding = True
            current.voting = False
            await message.channel.send(f"{messender} has opened responding!")
            await save_game_state(current)

        elif current.responding == True:
            await message.channel.send(f"Responding is already open! Did you mean to open voting?")
        elif messenderid != message.author.id:
            await message.channel.send(f"You must be the host to open responding!")
        elif current is None:
            await message.channel.send(f"There is no Write or Die to open responding to!")

    if command == 'respond':
        if current.responding == True:
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
                    await save_game_state(current)
        elif current is not None:
            await message.author.send("You can only respond during a responding period!")
        else:
            await message.author.send("You can only respond if a game has started!")

    if command == 'openvoting':
        if current is not None and messenderid == current.hostid and current.voting is False:
            current.voting = True
            current.responding = False
            await message.channel.send(f"{messender} has opened voting!")

            board = await generateBoard(current.responses, False)
            for i in current.playerid:
                await send_dm(i, board, client)
            await send_dm(current.hostid, "Voting has been sent out!", client)

            await save_game_state(current)


            
        elif current.voting == True:
            await message.channel.send(f"Responding is already open! Did you mean to open responding?")
        elif messenderid != message.author.id:
            await message.channel.send(f"You must be the host to open voting!")
        elif current is None:
            await message.channel.send(f"There is no Write or Die to open voting to!")

    if command == 'vote':
        if current is not None and current.voting == True:
            board = await generateBoard(current.responses, False)
            await message.channel.send(board)
        elif current is not None:
            await message.channel.send("You can only vote during a voting period!")
        else:
            await message.author.send("You can only vote if a game has started!")

    if command == 'end':
        if messenderid == current.hostid:
            success = await end_game()
            if success:
                await message.channel.send("The game has ended.")
            else:
                await message.channel.send("No game currently active.")
        else:
            await message.channel.send("You can only end the game if you are a host!")

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
