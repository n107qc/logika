import os 

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,QFileDialog, 
    QHBoxLayout, QVBoxLayout, QListWidget, QLineEdit, 
    QTextEdit, QInputDialog, QTableWidget,  QListWidgetItem,
    QFormLayout, QGroupBox, QButtonGroup, QRadioButton, QSpinBox,QMessageBox)

app = QApplication([])

window = QWidget()

btn_folder = QPushButton('Folder')

btn_left = QPushButton('Вліво')
btn_right = QPushButton('Вправо')
btn_flip = QPushButton('Перевернути')
btn_sharp = QPushButton("різкість")
btn_bw = QPushButton('Перетворити в чорнобіле')

lst_files = QListWidget()
lb_pic = QLabel('Картинки')

Layout1 = QHBoxLayout()
Layout2 = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_folder)
col1.addWidget(lst_files)

Layout2.addWidget(btn_left)
Layout2.addWidget(btn_right)
Layout2.addWidget(btn_flip)
Layout2.addWidget(btn_sharp)
Layout2.addWidget(btn_bw)

col2.addWidget(lb_pic)
col2.addLayout(Layout2)

Layout1.addLayout(col1, 1)
Layout1.addLayout(col2, 4)
window.setLayout(Layout1)

wordkir = QFileDialog.getExistingDirectory()

print(wordkir)

files_and_folders = os.listdir(wordkir)

print(files_and_folders)

def filter(files):
    result = []
    ext = ['jpg', 'jpeg', 'bmp', 'gif', 'jfif', 'svg', 'png']

    for file in files:
        if file.split('.')[-1] in ext:
            result.append(file)

    return result

print(filter(files_and_folders))

window.setLayout(Layout1)
window.show()
app.exec()