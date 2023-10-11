import sys
from PyQt6.QtWidgets import QApplication
from router import Router



if __name__ == "__main__":

    app = QApplication(sys.argv)

    router = Router()
    router.start()
    router.udp_sender.send("Hello, UDP Server!", "Info")

    app.exec()
