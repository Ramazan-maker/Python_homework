from PyQt6.QtCore import QThread, pyqtSignal
import socket

class MessageReceiver(QThread):
    message = pyqtSignal(str, str)

    def __init__(self, port):
        super().__init__()
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind(('localhost', self.port))
        self.running = False

    def run(self):
        self.running = True
        print(f"MessageReceiver is listening on port {self.port}")
        while self.running:
            message, client_address = self.server_socket.recvfrom(1024)
            message_text = message.decode()
            print(f"Received message from {client_address}: {message_text}")
            message_type = "Info"
            self.message.emit(message_text, message_type)

    def stop(self):
        self.running = False
        self.server_socket.close()



