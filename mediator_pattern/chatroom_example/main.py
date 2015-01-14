
from KChatroom import Chatroom
from KClient import Client

chatroom = Chatroom()

clientA = Client('Anders')
clientB = Client('Bengt')
clientC = Client('Carl')

clientA.Join(chatroom)
clientB.Join(chatroom)
clientC.Join(chatroom)

clientA.SendMessage('Hello, is anyone there?')
clientB.SendMessage('Hi, I am here.')
clientC.SendMessage('Me too.')