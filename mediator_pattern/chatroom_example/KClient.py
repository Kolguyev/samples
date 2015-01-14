

class Client(object):

    def __init__(self, name):
        self.name = name
        self.chatroom = None
        self.receivedMessages = list()

    def Name(self):
        return self.name

    def Join(self, chatroom):
        ''' Join a chat room '''
        self.chatroom = chatroom
        chatroom.AddClient(self)

    def SendMessage(self, message):
        ''' Uses a method of the chat room (Mediator) to send
            a message to clients, without knowing anything about
            who they are (that is handed over to the chat room to handle).
        '''
        self.chatroom.SendMessageToAll(self, message)

    def ReceivedMessages(self):
        return self.receivedMessages

    def AddReceivedMessage(self, message):
        self.receivedMessages.append(message)

