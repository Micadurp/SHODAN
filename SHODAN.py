#!/usr/bin/python3
from ChatConnector import ChatConnector as chatConnector

def main():
    chatHandler = chatConnector.ChatHandler()
    chatHandler.start()
    print("bye!")

if __name__ == '__main__':
    main()