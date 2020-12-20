import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') 

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    # break to stop infinte spam
    if message.author == client.user:
        return

    content = message.content.lower()
    response = ''

    if content == '!ping':
        response = 'pong'
    elif 'easy' in content:
        response = 'Not as easy as shopping online with Honey.'
    elif 'amazon' in content or 'newegg' in content:
        response = 'Consider shopping online with Honey.'
    elif 'lol' in content or 'lmao' in content:
        possibleChoices = [
            'I\'m not laughing.',
            'There\'s nothing funny about Honey.'
            'I don\'t get it.'
        ]
        response = random.choice(possibleChoices)

    if response != '':
        await message.channel.send(response)

client.run(TOKEN)