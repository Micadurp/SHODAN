#!/usr/bin/python3
import socket
from ..Config import ircConfig
import select

SOURCE = "irc"

class MsgHandler:
    send_general_message = None
    irc = None
    
    def __init__(self, general_send_message):
        self.send_general_message = general_send_message

    def checkforPing(self, p_checkforSec):
        ready = select.select([self.irc], [self.irc], [self.irc], p_checkforSec)
        if ready[0]:
            text = self.irc.recv(2040)
            text = text.decode('utf-8')
            print (text)
            
            if text.find('PING') != -1:
                print ("ping ponging")
                self.irc.send(bytes('PONG ' + text.split()[1] + '\r\n', 'utf-8'))
    
    def connect(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ("Connecting to " + ircConfig.SERVER)
        self.irc.connect((ircConfig.SERVER, 6667))
        print ("sending user")
        self.irc.send(bytes("USER "+ ircConfig.NICK +  " " + ircConfig.NICK + "2 " + ircConfig.NICK + "3 " + ircConfig.NICK + "3" + ircConfig.STOPSIGN, 'utf-8'))
        print ("sending nick")
        self.irc.send(bytes("NICK " + ircConfig.NICK + ircConfig.STOPSIGN, 'utf-8'))
        print ("joining channel")
        self.irc.send(bytes("JOIN " + ircConfig.CHANNEL + ircConfig.STOPSIGN, 'utf-8'))

    def process_messages(self):
        ready = select.select([self.irc], [self.irc], [self.irc], 1)
        if ready[0]:
            text = self.irc.recv(2040)
            text = text.decode('utf-8')
            if text.find('PRIVMSG') != -1:
                self.send_general_message(text, ircConfig.CHANNEL, SOURCE)
            if text.find('PING') != -1:
                print ("ping ponging")
                self.irc.send(bytes('PONG ' + text.split()[1] + '\r\n', 'utf-8'))

    def send_message(self, message):
        self.irc.send(bytes("PRIVMSG " + ircConfig.CHANNEL + " :" + message + ircConfig.STOPSIGN, 'utf-8'))
        print("irc message sent")