#!/usr/bin/python3
usingIRC = False
usingSlack = False
usingDiscord = False

try:
    import IRCHandler.ircHandler as ircHandler
    usingIRC = True
except ImportError:
    pass
    
try:
    import SlackHandler.slackHandler as slackHandler
    usingSlack = True
except ImportError:
    pass

try:
    import DiscordHandler.discordHandler as discordHandler
    usingDiscord = True
except ImportError:
    pass

if usingIRC:
    ircMsgHandler = ircHandler.MsgHandler()
    #ircMsgHandler.connect()

if usingSlack:
    slackHandler = slackHandler.MsgHandler()
    slackHandler.connect()

if usingDiscord:
    discordHandler = discordHandler.MsgHandler()
    discordHandler.connect()

    