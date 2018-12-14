#!/usr/bin/python3

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

    def send_messages(self, message, channel, source):
        print("Sending message from " + source)
        print("Target is " + channel + " though this is not yet implemented")
        print("Message is " + message)
        if usingSlack:
            if source != "slack":
                self.slackMsgHandler.send_message(message)
        if usingIRC:
            if source != "irc":
                self.ircMsgHandler.send_message(message)

    def start(self):

        if usingIRC: self.ircMsgHandler.connect()
        if usingSlack: self.slackMsgHandler.connect()
        
        while True:
            if usingIRC: self.ircMsgHandler.process_messages()
            if usingSlack: self.slackMsgHandler.process_messages()
        print("we quit now")