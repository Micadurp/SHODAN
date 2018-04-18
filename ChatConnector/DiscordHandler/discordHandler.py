#!/usr/bin/python3
import discord
import asyncio
from ..Config import discordConfig

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    msg = '{0.author}: {0.content}'.format(message)
    await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

class MsgHandler:
    genChatHandler = None

    def __init__(self, generalChatHandler):
        self.genChatHandler = generalChatHandler

    async def connect(self):
        await client.start(discordConfig.TOKEN)
    
    def logout(self):
        client.logout()

    def send_message(self, message):
        print("sending message to discord")
        for channel in client.get_all_channels():
            print(channel)
            if channel.name == "general":
                print("true?")
                print(message)
                client.send_message(channel, message)
        
