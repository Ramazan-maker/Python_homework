from PyQt6.QtCore import QThread, pyqtSlot
import socket

class MessageSender(QThread):
    def __init__(self, server_address, server_port):
        super().__init__()
        self.server_address = server_address
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.running = False

    @pyqtSlot(str, str)
    def send(self, text, type):
        message_to_send = f"{type}: {text}"
        self.client_socket.sendto(message_to_send.encode(), (self.server_address, self.server_port))

    def run(self):
        self.running = True


    def stop(self):
        self.running = False
        self.client_socket.close()
