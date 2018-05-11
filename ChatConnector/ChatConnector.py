#!/usr/bin/python3
import asyncio
from concurrent.futures import ThreadPoolExecutor

usingIRC = False
usingSlack = False
usingDiscord = False
try:
    from IRCHandler import ircHandler
    print("Using IRC")
    usingIRC = True
except ImportError:
    pass

try:
    from .SlackHandler import slackHandler
    print("Using Slack")
    usingSlack = True
except ImportError:
    pass

try:
    from .DiscordHandler import discordHandler
    print("Using Discord")
    usingDiscord = True
except ImportError:
    pass

class ChatHandler:
    def __init__(self):
        #self.ircMsgHandler = ircHandler.MsgHandler(self.send_messages)
        self.slackMsgHandler = slackHandler.MsgHandler(self.send_messages)
        self.discordMsgHandler = discordHandler.MsgHandler(self.send_messages)

    def send_messages(self, message, source):
        if source != "discord":
            self.discordMsgHandler.send_message(message)
        if source != "slack":
            self.slackMsgHandler.send_message(message)

    def start(self):       
        executor = ThreadPoolExecutor(2)
        loop = asyncio.get_event_loop()

        #if usingIRC:
            #ircMsgHandler.connect()

        if usingSlack:
            self.slackMsgHandler.connect()
            asyncio.ensure_future(loop.run_in_executor(executor, self.slackMsgHandler.read_chat))

        if usingDiscord:
            asyncio.ensure_future(self.discordMsgHandler.connect)

        try:
            loop.run_forever()
        except:
            print("eeeyyy")
            #discordHandler.logout()