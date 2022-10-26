from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QSizePolicy, QVBoxLayout, QMainWindow, QLineEdit, QPushButton, \
    QHBoxLayout, QGridLayout, QWidget, QFrame
import requests
from PyQt5.QtGui import QImage, QPixmap


# Sub-clase que hereda de QMainWindow
class VentanaPrincipal(QMainWindow):
    # constructor
    def __init__(self):
        super().__init__()
        self.container = QWidget()

        self.superior = QHBoxLayout()
        self.center = QGridLayout()
        self.center1 = QVBoxLayout()
        self.texto = QLineEdit()
        self.button = QPushButton("Buscar")
        self.image = QImage()
        self.image_label = QLabel()
        self.url_image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRR8sFD9yQ58vBr-2YGhPB6hyhF0hZKj2IlNaJBVQEKxViNlS6P'

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('uvFlix')
        self.image.loadFromData(requests.get(self.url_image).content)
        pixmap = QPixmap(self.image)
        pixmap2 = pixmap.scaledToWidth(200)
        self.image_label.setPixmap(pixmap2)
        self.superior.addWidget(self.texto)
        self.superior.addWidget(self.button)
        self.center.addWidget(self.image_label)
        self.center1.addLayout(self.superior)
        self.center1.addLayout(self.center)
        self.container.setLayout(self.center1)
        # self.container.setLayout(self.center)
        self.setCentralWidget(self.container)


if __name__ == '__main__':
    app = QApplication([])
    window = VentanaPrincipal()
    window.show()
    app.exec_()
