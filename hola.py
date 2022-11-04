from PyQt5.QtWidgets import QApplication, QLabel, QSizePolicy, QVBoxLayout, QMainWindow, QLineEdit, QPushButton, QHBoxLayout, QGridLayout, QWidget, QFrame
import requests
from PyQt5.QtGui import QImage, QPixmap
import threading

class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.container = QWidget()
        self.container2 = QWidget()

        self.superior = QHBoxLayout()
        self.center = QGridLayout()
        #self.center = QHBoxLayout()
        self.center1 = QVBoxLayout()

        self.texto = QLineEdit()
        self.button = QPushButton("Buscar")
        self.infor = [QPushButton("informacion"),
                      QPushButton("informacion"),
                      QPushButton("informacion"),
                      QPushButton("informacion"),
                      QPushButton("informacion")
                      ]
        self.image = [QImage(),
                      QImage(),
                      QImage(),
                      QImage(),
                      QImage()]
        self.image_label = [QLabel(),
                            QLabel(),
                            QLabel(),
                            QLabel(),
                            QLabel()]
        self.url_image = []
        self.id = None
        self.title = None
        self.description = None
        self.thread = threading.Thread(target=self.search_url)

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('uvFlix')
        self.resize(1000,350)

        self.texto.setFixedWidth(800)
        self.texto.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.button.setFixedWidth(50)
        self.button.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed))

        self.button.clicked.connect(lambda: self.thread.start())
        #self.infor.clicked.connect(lambda: self.click)

        self.superior.addWidget(self.texto)
        self.superior.addWidget(self.button)
        x=0
        for i in self.image_label:
            self.center.addWidget(i,1,x)
            x = x+1
        #self.center.addWidget(self.image_label, 1, 0)
        #self.center.addWidget(self.image_label2, 1, 2)
        #self.center.addWidget(self.image_label3, 1, 3)
       # self.center.addWidget(self.infor)

        self.center1.addLayout(self.superior)
        self.center1.addLayout(self.center)
        self.container.setLayout(self.center1)

        self.setCentralWidget(self.container)

    def search_url(self):
        d = 'https://clandestina-hds.com/movies/title?search='
        movies = self.texto.text().split(sep=',', maxsplit=5)
        t = []
        for h in movies:
            t.append(d+h)

        r = []

        for i in t:
            r.append(requests.get(i))

        data = []

        for q in r:
            data.append(q.json())

        data2 = []
        for v in data:
            data2.append(v['results'])

        data3 = []

        for n in data2:
            data3.append(n[0:3])

        for k in data3:
            self.url_image.append(k[1]['image'])
        x=0
        for m in self.image:
            m.loadFromData(requests.get(self.url_image[x]).content)
            pixmap = QPixmap(m)
            pixmap2 = pixmap.scaledToWidth(200)
            self.image_label[x].setPixmap(pixmap2)
            x = x + 1

    def click(self):
        self.image_label.show()


if __name__ == '__main__':
    app = QApplication([])
    window = VentanaPrincipal()
    window.show()
    app.exec_()