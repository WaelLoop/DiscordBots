import discord
import os
from datetime import datetime
#from Classes.database import PostgreSQL
from Classes.dub import Dub


# # database instance
# db = PostgreSQL('hostname', 'db', 'username', 'password')
# # Database table
# DB_TABLE = 'Discord'
# # Get wins from database command
# GET_DUB_COMMAND = f'SELECT wins FROM {DB_TABLE} WHERE date_field = %s'
# # Save wins to database command
# SAVE_DUB_COMMAND = f'INSERT INTO {DB_TABLE} (date_field, wins) VALUES (date, numWins)'

# client instance
client = discord.Client()
# dub instance
dub = Dub()
# Current date
currDate = datetime.now().strftime('%Y-%m-%d')

# List of commands that our bot will know
listOfCommands = [
    '!dub',
    '!gg',
    '!getdub <YYYY-MM-DD>'
    '!help',
]


@client.event
async def on_ready():
    print(f'We have logged in as {client}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Filter only messages that start with !message = "!command argument1 argument2"
    if message.startswith("!"):
        # split the message into individual parts
        parts = message.split()
        # remove the "!" character from the command name
        command = parts[0][1:].lower()
        # get any arguments (if applicable)
        arguments = parts[1:]
        
        # Match command with the list available
        if command == "dub":
            dub.incrementDub()
            await message.channel.send(f'Dub counter: {dub.getCounter()}')

        # Save the number of wins for the day to the database
        elif command == "gg":
            # Check if we have already gotten some wins
            # TODO: oldWins = db.read_data(GET_DUB_COMMAND.replace("%s", str(currDate)))
            totalWins = dub.getWins(currDate)
            totalWins += dub.getCounter()
            # Save the number of wins on the database
            # TODO: db.write_data(SAVE_DUB_COMMAND.replace("(date, numWins)", f'({currDate}, {currWins})'))
            dub.storeWins(totalWins, currDate)
            # Reset the counter
            dub.resetCounter()
            await message.channel.send(f'The number of wins the squad got today is {totalWins}... GGs')

        # Get the number of wins by providing a specific date in the format dd/mm/yy
        elif command == "getdub":
            # TODO: wins = db.read_data(GET_DUB_COMMAND.replace("%s", arguments))
            try:
                datetime.strptime(arguments, '%Y-%m-%d')
                wins = dub.getWins(arguments)
                await message.channel.send(f'The numbers of dubs the squad got on {arguments}: {wins}')
            except ValueError:
                await message.channel.send(f'Invalid date format. The date must be in the format YYYY-MM-DD')

        # Help command to display available commands
        elif command == "help":
            response = "Below is the list of valid commands:\n" + "\n".join(str(command) for command in listOfCommands)
            await message.channel.send(response)

        # Invalid command
        else:
            await message.channel.send(f'Not a valid command. Try "!help" to see the list of commands')


client.run(os.getenv('TOKEN'))