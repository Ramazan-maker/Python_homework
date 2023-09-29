
import threading
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtCore import QObject, pyqtSignal

class MyApp(QWidget, QObject):
    def __init__(self):
        super().__init__()
        self.filename = "input.txt"
        self.text = ""

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        self.button = QPushButton("Открыть", self)
        self.button.clicked.connect(self.open_file)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text_edit)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.text_readed.connect(self.text_edit.setText)

        self.show()

    text_readed = pyqtSignal(str)

    def open_file(self):
        thread = threading.Thread(target=self.read_file)
        thread.start()

    def read_file(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            self.text = f.read()
            self.text_readed.emit(self.text)

if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    app.exec()
