import os
from dotenv import load_dotenv
import bot as client

load_dotenv()

bot_secret = os.getenv('TOKEN')


@client.event
async def on_ready():
    print('The bot is ready {0.user}'.format(client))


@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if channel.name == 'Main':
            await channel.send('Welcome {}'.format(member.mention))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for mention in message.mentions:
        if mention.id == client.user.id:
            await message.reply('Hi! How are you?')
            break


client.run(bot_secret)
