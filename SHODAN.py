#!/usr/bin/python3
import asyncio
from concurrent.futures import ThreadPoolExecutor

def main():
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
    
    executor = ThreadPoolExecutor(2)
    loop = asyncio.get_event_loop()

    try:
        asyncio.ensure_future(loop.run_in_executor(executor, slackHandler.read_chat))
        asyncio.ensure_future(loop.run_in_executor(executor, discordHandler.connect))
        loop.run_forever()
    except:
        discordHandler.logout()

if __name__ == '__main__':
    main()