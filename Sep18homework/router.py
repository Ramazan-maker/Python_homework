from PyQt6.QtCore import QObject
from udp_receiver import MessageReceiver

from udp_sender import MessageSender




class Router(QObject):
    def __init__(self):
        super().__init__()
        self.udp_receiver = MessageReceiver(9900)
        self.udp_sender = MessageSender('localhost', 9900)

    def start(self):
        self.udp_receiver.start()
        self.udp_sender.start()

    def stop(self):
        self.udp_receiver.stop()
        self.udp_sender.stop()