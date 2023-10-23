import os 

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,QFileDialog, 
    QHBoxLayout, QVBoxLayout, QListWidget, QLineEdit, 
    QTextEdit, QInputDialog, QTableWidget,  QListWidgetItem,
    QFormLayout, QGroupBox, QButtonGroup, QRadioButton, QSpinBox,QMessageBox)

app = QApplication([])

window = QWidget()



btn_folder = QPushButton('Folderψ(._. )>')

btn_left = QPushButton('Вліво(ಥ _ ಥ)')
btn_right = QPushButton('Вправоo(〃＾▽＾〃)o')
btn_flip = QPushButton('Перевернути(⓿_⓿)')
btn_sharp = QPushButton("різкістьლ(╹◡╹ლ)")
btn_bw = QPushButton('Перетворити в чорнобіле◑﹏◐')

lst_files = QListWidget()
lb_pic = QLabel('Картинки(^人^)')

window.setStyleSheet('''
                        background-color: AliceBlue;
                        color: Navy;
                        font-size: 20px;
                        border: 2px solid Indigo; 
                        ''')

btn_folder.setStyleSheet('''
                        background-color: MediumOrchid;
                        color: Black;
                        font-size: 20px;
                        border: 2px solid Indigo; 
                        ''')

btn_left.setStyleSheet('''
                        background-color: Lime;
                        color: MediumVioletRed;
                        font-size: 20px;
                        border: 2px solid Indigo; 
                        ''')

btn_right.setStyleSheet('''
                        background-color: Tomato;
                        color: Turquoise;
                        font-size: 20px;
                        border: 2px solid Indigo; 
                        ''')

btn_flip.setStyleSheet('''
                        background-color: DarkGoldenRod;
                        color: Black;
                        font-size: 20px;
                        border: 2px solid Indigo; 
                        ''')

btn_sharp.setStyleSheet('''
                        background-color: Crimson;
                        color: Black;
                        font-size: 20px;
                        border: 2px solid Indigo; 
                        ''')

btn_sharp.setStyleSheet('''
                        background-color: Crimson;
                        color: Black;
                        font-size: 20px;
                        border: 2px solid Indigo; 
                        ''')

btn_bw.setStyleSheet('''
                        background-color: LightSeaGreen;
                        color: NavajoWhite;
                        font-size: 20px;
                        border: 2px solid Indigo; 
                        ''')

btn_bw.setStyleSheet('''
                        background-color: LightSeaGreen;
                        color: NavajoWhite;
                        font-size: 20px;
                        border: 2px solid Indigo; 
                        ''')

lst_files.setStyleSheet('''
                        background-color: PaleVioletRed;
                        color: MediumVioletRed;
                        font-size: 20px;
                        border: 2px solid Indigo; 
                        ''')

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