import discord
import os
from datetime import datetime, timedelta


# Dub instance
class Dub:
  # Constructor
  def __init__(self):
    self.counter = 0
  
  # Function that increments the counter variable
  def increment_dub(self):
    self.counter += 1

  def reset_counter(self):
    self.counter = 0

# client instance
client = discord.Client()

# our dub instance
dub = Dub()

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

  elif message.content.startswith('!tmu'):
    """
      How to use: !tmu
      What it does: Sends a hype message. #TMU
    """
    await message.channel.send('TURN ME UPPPPPPPPPPPP')
  
  elif message.content.startswith('!reset'):
    """
      How to use: !reset
      What it does: Sets the counter attribute of the dub instance to 0
    """
    dub.reset_counter()
    await message.channel.send(f'The dub counter has been reset! Current dub counter: {dub.counter}')


client.run(os.getenv('TOKEN'))
