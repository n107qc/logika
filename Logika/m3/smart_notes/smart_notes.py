# основа🥟
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, 
    QHBoxLayout, QVBoxLayout, QListWidget, QLineEdit, 
    QTextEdit, QInputDialog, QTableWidget,  QListWidgetItem,
    QFormLayout, QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json

def writeToFile():
    with open('note.json', 'w', encoding='utf8') as file:
        json.dump(notes, file, ensure_ascii=False, sort_keys=True, indent=4)

app = QApplication([])

window = QWidget()




filed_text = QTextEdit()
lb_notes = QLabel("Список Заміток ༼ つ ◕_◕ ༽つ🥖")
lst_notes = QListWidget()

# верхні кнопочки
btn_note_create = QPushButton("Створити ψ(｀∇´)ψ🍼")
btn_note_delete = QPushButton("Видалити O(∩_∩)O🥓")
btn_note_save = QPushButton("Зберигти \^o^/🥩")

filed_tag = QLineEdit()
lb_tags = QLabel('Список Тегів (～￣▽￣)～🥂')
lst_tags = QListWidget()


# нижні кнопочки
btn_tag_add_notes = QPushButton("Додати до замітки ◑﹏◐☕")
btn_tag_unpin = QPushButton("Відкріпити від замітки (✿◕‿◕✿)🥞")
btn_tag_search_teg = QPushButton("Шукати замітки за тегом (★ ω ★)🍕")

window.setStyleSheet('''
                        background-color: AliceBlue;
                        color: Navy;
                        font-size: 20px;
                        border: 2px solid Indigo; 
                        ''')

lst_notes.setStyleSheet('''
                        background-color: CornflowerBlue;
                        color: DarkBlue;
                        font-size: 20px;
                        border: 2px solid Chartreuse; 
                        ''')

btn_note_create.setStyleSheet('''
                        background-color: Crimson;
                        color: DarkSlateGrey;
                        font-size: 20px;
                        border: 2px solid DimGrey; 
                        ''')

btn_note_delete.setStyleSheet('''
                        background-color: OrangeRed;
                        color: Purple;
                        font-size: 20px;
                        border: 2px solid Teal; 
                        ''')

btn_note_save.setStyleSheet('''
                        background-color: DarkMagenta;
                        color: DarkRed;
                        font-size: 20px;
                        border: 2px solid Indigo; 
                        ''')


lst_tags.setStyleSheet('''
                        background-color: CornflowerBlue;
                        color: Coral;
                        font-size: 20px;
                        border: 2px solid DarkOliveGreen; 
                        ''')


btn_tag_add_notes.setStyleSheet('''
                        background-color: Khaki;
                        color: LightCoral;
                        font-size: 20px;
                        border: 2px solid LightGoldenRodYellow; 
                        ''')

btn_tag_unpin.setStyleSheet('''
                        background-color: Green;
                        color: IndianRed;
                        font-size: 20px;
                        border: 2px solid DarkSlateGrey; 
                        ''')

btn_tag_search_teg.setStyleSheet('''
                        background-color: CornflowerBlue;
                        color: BlueViolet;
                        font-size: 20px;
                        border: 2px solid Coral; 
                        ''')

loyout_notes = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

loyout_notes.addLayout(col1, stretch=2)
loyout_notes.addLayout(col2, stretch=1)

col1.addWidget(filed_text)
col2.addWidget(lb_notes)
col2.addWidget(lst_notes)
col2.addWidget(btn_note_create)
col2.addWidget(btn_note_delete)
col2.addWidget(btn_note_save)

col2.addWidget(lb_tags)
col2.addWidget(lst_tags)
col2.addWidget(filed_tag)
col2.addWidget(btn_tag_add_notes)
col2.addWidget(btn_tag_unpin)
col2.addWidget(btn_tag_search_teg)

def show_notes():
    key = lst_notes.currentItem().text()
    filed_text.setText(notes[key]['текст'])

    lst_tags.clear()
    lst_tags.addItems(notes[key]['теги'])

def add_note():
    note_name, ok = QInputDialog.getText(window, 'Додати Замітку', 'Нова замітка')
    if note_name and ok:
        lst_notes.addItem(note_name)
        notes[note_name] = {'текст': "", "теги": []}

        writeToFile()
        
def del_note():
    if lst_notes.currentItem():
        key = lst_notes.currentItem().text()
        del notes[key]

        filed_text.clear()
        lst_tags.clear()
        lst_notes.clear()
        lst_notes.addItems(notes)

        writeToFile()

    else:
        print("НЕЗЯ")

def save_note():
    if lst_notes.currentItem():
        key = lst_notes.currentItem().text()
        notes[key]['текст'] = filed_text.toPlainText()

        writeToFile()

btn_note_save.clicked.connect(save_note)
btn_note_delete.clicked.connect(del_note)
btn_note_create.clicked.connect(add_note)
lst_notes.itemClicked.connect(show_notes)

with open('note.json', 'r' , encoding = 'utf8') as file:
    notes = json.load(file)

lst_notes.addItems(notes)    


window.setLayout(loyout_notes)
window.show()
app.exec()