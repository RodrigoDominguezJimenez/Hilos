from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QLineEdit, QPushButton, QWidget


class VentanaPrincipal(QMainWindow):
    # constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Peliculas piratas")
        layout = QHBoxLayout()

        buscar = QHBoxLayout()

        self.bbuscar = QLineEdit()
        buscar.addWidget(self.bbuscar)
        self.bbuscar = QPushButton("Buscar")
        buscar.addWidget(self.bbuscar)

        layout.addLayout(buscar)

        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)


app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec_()
