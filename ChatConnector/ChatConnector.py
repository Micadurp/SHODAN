#!/usr/bin/python3
import asyncio
from concurrent.futures import ThreadPoolExecutor

usingIRC = False
usingSlack = False

try:
    from .IRCHandler import ircHandler
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

class ChatHandler:
    def __init__(self):
        if usingIRC:
            self.ircMsgHandler = ircHandler.MsgHandler(self.send_messages)
        if usingSlack:
            self.slackMsgHandler = slackHandler.MsgHandler(self.send_messages)

    def send_messages(self, message, source):
        
        if usingSlack:
            if source != "slack":
                self.slackMsgHandler.send_message(message)
        if usingIRC:
            if source != "irc":
                self.ircMsgHandler.send_message(message)

    def start(self):       
        executor = ThreadPoolExecutor(2)
        loop = asyncio.get_event_loop()

        if usingIRC:
            self.ircMsgHandler.connect()

        if usingSlack:
            self.slackMsgHandler.connect()
            asyncio.ensure_future(loop.run_in_executor(executor, self.slackMsgHandler.read_chat))
        