from PyQt6.QtCore import QThread
from udp_client import UDP_Client

class MessageSender():
    def __init__(self):
        super.__init__()

    def send(self,  text, type):
        udp_client = UDP_Client('localhost', 1)
        message = f"{type}:{text}"
        udp_client.send(message)
        udp_client.close()