
import unittest

class TestMediator(unittest.TestCase):

    def tests_Client(self):
        from KClient import Client
        client = Client('Anders')
        self.assertNotEqual(client, None)
        self.assertEqual(client.Name(), 'Anders')

    def test_Chatroom(self):
        from KClient import Client
        clientA = Client('Anders')
        clientB = Client('Bertil')
        from KChatroom import Chatroom
        chatroom = Chatroom()
        clientA.Join(chatroom)
        self.assertTrue(clientA in chatroom.Clients())
        clientB.Join(chatroom)
        self.assertTrue(clientB in chatroom.Clients())
        messageToSend = 'Hello, this is Anders.'
        messageToReceive = 'Anders: Hello, this is Anders.'
        clientA.SendMessage(messageToSend)
        self.assertTrue(messageToReceive in clientB.ReceivedMessages())


unittest.main()