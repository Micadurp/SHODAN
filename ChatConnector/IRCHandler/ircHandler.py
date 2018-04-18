#!/usr/bin/python3
import socket
import Config.ircConfig as ircConfig
import select

class MsgHandler:
    def connect(self):
        irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ("Connecting to " + ircConfig.server)
        irc.connect((ircConfig.server, 6667))