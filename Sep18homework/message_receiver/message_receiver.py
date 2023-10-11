from PyQt6.QtCore import QThread, pyqtSignal
from udp_server.udp_server import UDP_Server


class MessageReciever(QThread):
    message = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()

    def run(self):
        server = UDP_Server()
        text = server.get_message_text()
        type = server.get_message_type()

        self.message.emit(text, type)


