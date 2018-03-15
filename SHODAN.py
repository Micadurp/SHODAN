#!/usr/bin/python3
usingIRC = False

try:
    import IRCHandler.ircHandler as ircHandler
    usingIRC = True
except ImportError:
    pass

if usingIRC:
    ircMsgHandler = ircHandler.MsgHandler()
    ircMsgHandler.connect()