import discord
import os
from datetime import datetime

# Dub instance
class Dub:
  # Constructor
  def __init__(self):
    # Number of dubs we get a day
    self.counter = 0
    # Our hash map that keeps track of our daily dubs throughout the years
    self.history = {}

  # Function that increments the counter variable
  def increment_dub(self):
    """Increments the counter attribute"""
    self.counter += 1

  def reset_counter(self, date):
    """ Saves the number of dubs we get for today and resets the counter"""
    # save the number of dubs pertaining to today
    self.history[date] = self.counter
    # reset the number of dubs
    self.counter = 0

  def get_dubs(self, date):
    """Returns the number of dubs for a certain date"""
    return self.history[date]


# client instance
client = discord.Client()

# our dub instance
dub = Dub()

# List of commands that our bot will know
listOfCommands = {
    "!wael": "Game: ENEMY DROPPING TO THE AO.\nWael: Down",
    "!yousef": "your wife beater friend, of course",
    "!huy": 'Repeat after me: "Ashhadu An Laa"',
    "!abdul": "ABDUL THE PUSHER! A.K.A. 14 Kills Coach Abdul",
    "!tmu": 'TURN ME THE FUCK UPPPPPPPPPPPP YABNIL LATHIIIIIIINNAAAAAAAAAAAAA',
    "!grau": 'Mono suppressor\nTempus 26.4 Arch\nTac Laser\nCommando Foregrip\n50 Round Mag',
    "!alex": "What does Alex say when he gets downed on a dumb push...\n\nOMG WALLAH HE'S 1 SHOT",
    "!talal": "YEL3AN OM EL KHARA"
}


@client.event
async def on_ready():
  print(f'We have logged in as {client}')


@client.event
async def on_message(message):
  if message.author == client.user:
      return

  if message.content.startswith('!dub'):
    """
      How to use: !dub
      What it does: increments the counter attribute of the dub instance.
    """
    dub.increment_dub()
    await message.channel.send(f'Dub counter: {dub.counter}')

  elif message.content.startswith('!reset'):
    """
      How to use: !reset
      What it does: Sets the counter attribute of the dub instance to 0
    """
    # Get the current dub counter
    dubsToday = dub.counter
    # Get today's date. DD/MM/YY
    today = datetime.today().strftime("%d/%m/%y")
    # Reset the counter
    dub.reset_counter(today)
    await message.channel.send(f'The number of dubs we got on {today}: {dubsToday}\n GGs')

  elif message.content.startswith("!help"):
    """
      How to use: !help
      What it does: prints the list of valid commands
    """
    otherCommands = ["!dub", "!reset", "!GetDub <DD/MM/YY>", "!help"]  # The ones that requires access to the hashmap
    validCommands = list(listOfCommands.keys())
    validCommands.append(otherCommands)
    response = "Here is the list of valid commands:\n\t" + "\n\t".join(validCommands)
    await message.channel.send(response)

  try:
      response = listOfCommands[message]
      await message.channel.send(response)
  except KeyError:
      await message.channel.send("Not a valid command. Try !help to see the list of valid commands")


client.run(os.getenv('TOKEN'))
