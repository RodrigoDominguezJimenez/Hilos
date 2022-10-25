from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QLineEdit, QPushButton, QWidget


class main_window (QMainWindow):
    # constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Peliculas piratas")
        layout = QHBoxLayout()

        search = QHBoxLayout()

        self.ssearch = QLineEdit()
        search.addWidget(self.ssearch)
        self.ssearch = QPushButton("Buscar")
        search.addWidget(self.ssearch)

        layout.addLayout(search)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


app = QApplication([])
window = main_window ()
window.show()
app.exec_()
