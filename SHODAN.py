#!/usr/bin/python3
import asyncio
from concurrent.futures import ThreadPoolExecutor
import ChatConnector.GeneralChatHandler.generalChatHandler as generalChatHandler

def main():
    usingIRC = False
    usingSlack = False
    usingDiscord = False

    try:
        import ChatConnector.IRCHandler.ircHandler as ircHandler
        print("Using IRC")
        usingIRC = True
    except ImportError:
        pass

    try:
        import ChatConnector.SlackHandler.slackHandler as slackHandler
        print("Using Slack")
        usingSlack = True
    except ImportError:
        pass

    try:
        import ChatConnector.DiscordHandler.discordHandler as discordHandler
        print("Using Discord")
        usingDiscord = True
    except ImportError:
        pass

    genChatHandler = generalChatHandler.MsgHandler()
    #if usingIRC:
        # ircMsgHandler = ircHandler.MsgHandler(genChatHandler)
        # ircMsgHandler.connect()

    if usingSlack:
        slackHandler = slackHandler.MsgHandler(genChatHandler)
        slackHandler.connect()

    if usingDiscord:
        discordHandler = discordHandler.MsgHandler(genChatHandler)
        genChatHandler.setDiscordHandler(discordHandler)
    
    executor = ThreadPoolExecutor(2)
    loop = asyncio.get_event_loop()

    try:
        asyncio.ensure_future(loop.run_in_executor(executor, slackHandler.read_chat))
        asyncio.ensure_future(discordHandler.connect)
        loop.run_forever()
    except:
        discordHandler.logout()

if __name__ == '__main__':
    main()