from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QLabel ,QSizePolicy, QVBoxLayout, QMainWindow, QLineEdit, QPushButton, QHBoxLayout, QGridLayout, QWidget, QFrame
import requests
from PyQt5.QtGui import QImage, QPixmap

# Sub-clase que hereda de QMainWindow
class VentanaPrincipal(QMainWindow):
    # constructor
    def __init__(self):
        super().__init__()
        self.container = QWidget()
        self.container2 = QWidget()

        self.superior = QHBoxLayout()
        self.center = QGridLayout()
        self.center1 = QVBoxLayout()

        self.texto = QLineEdit()
        self.button = QPushButton("Buscar")
        self.image = QImage()
        self.image_label = QLabel()
        self.url_image = []

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('uvFlix')
        self.setSizePolicy(500,400)

        self.texto.setFixedWidth(100)
        self.texto.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.button.clicked.connect(lambda: self.search_url())

        self.superior.addWidget(self.texto)
        self.superior.addWidget(self.button)
        self.center.addWidget(self.image_label)

        self.center1.addLayout(self.superior)
        self.center1.addLayout(self.center)
        self.container.setLayout(self.center1)

        url = self.url_image[1]
        self.image.loadFromData(requests.get(url).content)
        pixmap = QPixmap(self.image)
        pixmap2 = pixmap.scaledToWidth(200)
        self.image_label.setPixmap(pixmap2)

        self.setCentralWidget(self.container)

    def search_url(self):
        d = 'https://clandestina-hds.com/movies/title?search='
        t = d + self.texto.text()
        r = requests.get(t)
        data = r.json()
        data2 = data['results']
        data3 = data2[0:3]
        for i in data3:
            self.url_image.append(i['image'])


if __name__ == '__main__':
    app = QApplication([])
    window = VentanaPrincipal()
    window.show()
    app.exec_()