from PyQt5.QtWidgets import QApplication, QLabel, QSizePolicy, QVBoxLayout, QMainWindow, QLineEdit, QPushButton, QHBoxLayout, QGridLayout, QWidget, QFrame
import requests
from PyQt5.QtGui import QImage, QPixmap
import threading

class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.windowTwo = QMainWindow()

        self.container = QWidget()
        self.container2 = QWidget()
        self.superior = QHBoxLayout()
        self.center = QGridLayout()
        self.center1 = QVBoxLayout()

        self.container_two= QWidget()
        self.center_two = QVBoxLayout()

        self.texto = QLineEdit()
        self.button = QPushButton("Buscar")
        self.infor = QPushButton("informacion")
        self.infor2 = QPushButton("informacion")
        self.infor3 = QPushButton("informacion")
        self.infor4 = QPushButton("informacion")
        self.infor5 = QPushButton("informacion")
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
        self.url_image = None
        self.id = [None,
                   None,
                   None,
                   None,
                   None]
        self.id_label = QLabel()
        self.title = [None,
                      None,
                      None,
                      None,
                      None]
        self.title_label = QLabel()
        self.description = [None,
                            None,
                            None,
                            None,
                            None]
        self.description_label = QLabel()
        self.runTime = [None,
                        None,
                        None,
                        None,
                        None]
        self.runTime_label = QLabel()
        self.plot = [None,
                     None,
                     None,
                     None,
                     None]
        self.plot_label = QLabel()
        self.thread = threading.Thread(target=self.search_url)
        self.num = 0

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('uvFlix')
        self.resize(1000,350)

        self.texto.setFixedWidth(800)
        self.texto.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.button.setFixedWidth(50)
        self.button.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed))

        self.button.clicked.connect(lambda: self.thread.start())
        self.infor.clicked.connect(lambda: self.click(0))
        self.infor2.clicked.connect(lambda: self.click(1))
        self.infor3.clicked.connect(lambda: self.click(2))
        self.infor4.clicked.connect(lambda: self.click(3))
        self.infor5.clicked.connect(lambda: self.click(4))

        self.superior.addWidget(self.texto)
        self.superior.addWidget(self.button)
        x=0
        for i in self.image_label:
            self.center.addWidget(i,1,x)
            x = x+1
        self.center.addWidget(self.infor,2,0)
        self.center.addWidget(self.infor2, 2, 1)
        self.center.addWidget(self.infor3, 2, 2)
        self.center.addWidget(self.infor4, 2, 3)
        self.center.addWidget(self.infor5, 2, 4)

        self.center1.addLayout(self.superior)
        self.center1.addLayout(self.center)
        self.container.setLayout(self.center1)

        self.setCentralWidget(self.container)

    def search_url(self):
        movies = self.texto.text().split(sep=',', maxsplit=5)
        thread_lst = []

        x = 0

        for i in movies:
            thread_lst.append(threading.Thread(target=self.search_movie, args=(i,x)))
            x = x+1

        for j in thread_lst:
            j.start()
            #j.join()

    def search_movie(self,title, num):
        url = 'https://clandestina-hds.com/movies/title?search='
        url2 = url + title

        r = requests.get(url2)

        data = r.json()
        data2 = data['results']
        data3 = data2[0:3]

        self.url_image = data3[0]['image']
        self.id[num] = data3[0]['id']
        self.title[num] = (data3[0]['title'])
        self.description[num] = data3[0]['description']
        self.runTime[num] = data3[0]['runtimeStr']
        self.plot[num] = data3[0]['plot']

        self.image[num].loadFromData(requests.get(self.url_image).content)
        pixmap = QPixmap(self.image[num])
        pixmap2 = pixmap.scaledToWidth(200)
        self.image_label[num].setPixmap(pixmap2)



    def click(self,num):
        x = num
        self.windowTwo.setWindowTitle('Informacion')

        iD = 'id: ' + self.id[x]
        self.id_label.setText(iD)

        title = 'Tittle: ' + self.title[x]
        self.title_label.setText(title)

        description = 'Description: ' + self.description[x]
        self.description_label.setText(description)

        runTime = 'Run time: ' + self.runTime[x]
        self.runTime_label.setText(runTime)

        plot = 'Plot: ' + self.plot[x]
        self.plot_label.setText(plot)

        self.center_two.addWidget(self.id_label)
        self.center_two.addWidget(self.title_label)
        self.center_two.addWidget(self.description_label)
        self.center_two.addWidget(self.runTime_label)
        self.center_two.addWidget(self.plot_label)


        self.container_two.setLayout(self.center_two)

        self.windowTwo.setCentralWidget(self.container_two)
        self.windowTwo.show()


if __name__ == '__main__':
    app = QApplication([])
    window = VentanaPrincipal()
    window.show()
    app.exec_()

    #moana, jumanji, frozen, Big Hero 6, Inside Out