import os 

import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel, 
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget, QListWidgetItem, QFormLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox,QFileDialog,QAction)
from PyQt5.QtGui import QKeySequence
from PIL import Image, ImageFilter

from PyQt5.QtGui import QPixmap,QIcon
app = QApplication([])

window = QWidget()



btn_folder = QPushButton('Folderψ(._. )>')

btn_left = QPushButton('Вліво(ಥ _ ಥ)')
btn_right = QPushButton('Вправоo(〃＾▽＾〃)o')
btn_flip = QPushButton('Перевернутиฅʕ•̫͡•ʔฅ')
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

wordkir = ""

def filter(files):
    result = []
    ext = ['jpg', 'jpeg', 'bmp', 'gif', 'jfif', 'svg', 'png']

    for file in files:
        if file.split('.')[-1] in ext:
            result.append(file)

    return result

def showFiles():
    global wordkir

    wordkir = QFileDialog.getExistingDirectory()
    files_and_folders = os.listdir(wordkir)
    
    #['sunflower.jfif', 'vergil.jpg', 'main1.py']
    filterered_img = filter(files_and_folders)

    lst_files.clear()
    lst_files.addItems(filterered_img)

class imageProcessor():
    def __init__(self):
        self.filename = None
        self.original = None
        self.save_dir = 'Modified/'

    def loadImage(self, filename):
        self.filename = filename
        full_path = os.path.join(wordkir, filename)
        self.original = Image.open(full_path)
        
    def show_image(self, path):
        lb_pic.hide()

        pixmapimage = QPixmap(path)
        w, h = lb_pic.width(), lb_pic.height()

        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)

        lb_pic.setPixmap(pixmapimage)
        lb_pic.show()

def showChosenImage():
    filename = lst_files.currentItem().text()
    workimage.loadImage(filename)
    full_path = os.path.join(wordkir, filename)
    workimage.show_image(full_path)

workimage = imageProcessor()

lst_files.itemClicked.connect(showChosenImage)

btn_folder.clicked.connect(showFiles)
window.setLayout(Layout1)
window.show()
app.exec()