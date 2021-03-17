import discord
import os
from datetime import date

# client instance
client = discord.Client()


@client.event
async def on_ready():
    print(f'We have logged in as {client}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # TODO:
    #   ADD-ON: ADD A VICTORY SONG
    if message.content.lower().startswith('!dub'):
        await message.channel.send('Hello!')

    # TODO:
    #   IDEA: PLAY A SONG
    if message.content.lower().startwith('TURN ME UP'):
        await message.channel.send('TURN ME THE FUCK UPPPPPPPPPPPP')


client.run(os.getenv('TOKEN'))
