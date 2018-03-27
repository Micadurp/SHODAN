#!/usr/bin/python3
usingIRC = False
usingSlack = False
usingDiscord = False

try:
    import IRCHandler.ircHandler as ircHandler
    print("Using IRC")
    usingIRC = True
except ImportError:
    pass

try:
    import SlackHandler.slackHandler as slackHandler
    print("Using Slack")
    usingSlack = True
except ImportError:
    pass

try:
    import DiscordHandler.discordHandler as discordHandler
    print("Using Discord")
    usingDiscord = True
except ImportError:
    pass

if usingIRC:
    ircMsgHandler = ircHandler.MsgHandler()
    # ircMsgHandler.connect()

if usingSlack:
    slackHandler = slackHandler.MsgHandler()
    slackHandler.connect()


if usingDiscord:
    discordHandler = discordHandler.MsgHandler()
    discordHandler.connect()

while True:
    if usingSlack:
        slackHandler.read_chat()
