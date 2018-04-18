#!/usr/bin/python3


class MsgHandler:
    discordHandler = None
    slackHandler = None
    ircHandler = None

    def setDiscordHandler(self, discHandler):
        self.discordHandler = discHandler

    def setSlackHandler(self, slaHandler):
        self.slackHandler = slaHandler

    def send_messages(self, message):
        self.discordHandler.send_message(message)
        #self.slackHandler.send_message(message)