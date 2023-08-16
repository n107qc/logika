from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton

app = QApplication([])
main_win = QWidget()

label = QLabel("Коли началась Висадка у НормандіЇ")

radio_button1 = QRadioButton("6 червня 1944 року")
radio_button2 = QRadioButton("27 листопад 1943 року")
radio_button3 = QRadioButton("12 вересня 1939 року")
radio_button4 = QRadioButton("4 січня 1945 року")

layoutV = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layoutH1.addWidget(label,alignment=Qt.AlignCenter)
layoutH2.addWidget(radio_button1,alignment=Qt.AlignCenter)
layoutH2.addWidget(radio_button3,alignment=Qt.AlignCenter)
layoutH3.addWidget(radio_button2,alignment=Qt.AlignCenter)
layoutH3.addWidget(radio_button4,alignment=Qt.AlignCenter)

layoutV.addLayout(layoutH1)
layoutV.addLayout(layoutH2)
layoutV.addLayout(layoutH3)

def lose():
    a = QMessageBox()
    a.setText('згадай підручник за 10 клас')
    a.exec_()
radio_button3.clicked.connect(lose)
radio_button2.clicked.connect(lose)
radio_button4.clicked.connect(lose)

def win():
    a = QMessageBox()
    a.setText('Згадав підручник за 10 клас')
    a.exec_()
radio_button1.clicked.connect(win)

main_win.setLayout(layoutV)

main_win.show()
app.exec_()
