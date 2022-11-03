from PyQt5.QtCore import Qt,pyqtSignal,QTimer
from PyQt5.QtWidgets import QApplication, QLabel, QSizePolicy, QVBoxLayout, QMainWindow, QLineEdit, QPushButton, QHBoxLayout, QGridLayout, QWidget, QFrame
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
        self.infor = QPushButton("informacion")
        self.image = QImage()
        self.image_label = QLabel()
        self.image_label2 = QLabel()
        self.image_label3 = QLabel()
        self.url_image = None
        self.id = None
        self.title = None
        self.description = None

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('uvFlix')
        self.resize(500,350)

        self.texto.setFixedWidth(400)
        self.texto.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.button.clicked.connect(lambda: self.search_url())
        #self.infor.clicked.connect(lambda: self.click)

        self.superior.addWidget(self.texto)
        self.superior.addWidget(self.button)
        self.center.addWidget(self.image_label, 1, 1)
        self.center.addWidget(self.image_label2, 1, 2)
        self.center.addWidget(self.image_label3, 1, 3)
        self.center.addWidget(self.infor)

        self.center1.addLayout(self.superior)
        self.center1.addLayout(self.center)
        self.container.setLayout(self.center1)

        self.setCentralWidget(self.container)

    def search_url(self):
        d = 'https://clandestina-hds.com/movies/title?search='
        t = d + self.texto.text()
        r = requests.get(t)
        data = r.json()
        data2 = data['results']
        data3 = data2[0:3]
        self.url_image = data3[1]['image']
        self.id = data3[1]['id']
        self.title = data3[1]['title']
        self.description = data3[1]['description']
        self.image.loadFromData(requests.get(self.url_image).content)
        pixmap = QPixmap(self.image)
        pixmap2 = pixmap.scaledToWidth(200)
        self.image_label.setPixmap(pixmap2)

    def click(self):
        self.image_label.show()


if __name__ == '__main__':
    app = QApplication([])
    window = VentanaPrincipal()
    window.show()
    app.exec_()