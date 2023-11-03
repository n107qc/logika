# основа🥟
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, 
    QHBoxLayout, QVBoxLayout, QListWidget, QLineEdit, 
    QTextEdit, QInputDialog, QTableWidget,  QListWidgetItem,
    QFormLayout, QGroupBox, QButtonGroup, QRadioButton, QSpinBox,QMessageBox)
import json

def saveToFile():
    with open('note.json', 'w', encoding='utf8') as file:
        json.dump(notes, file, ensure_ascii=False, sort_keys=True, indent=4)

app = QApplication([])

window = QWidget()




filed_text = QTextEdit()
lb_notes = QLabel("Список Заміток ༼ つ ◕_◕ ༽つ🥖")
lst_notes = QListWidget()

# верхні кнопочки
btn_note_create = QPushButton("Створити ψ(｀∇´)ψ🍰")
btn_note_delete = QPushButton("Видалити O(∩_∩)O🥓")
btn_note_save = QPushButton("Зберигти \^o^/🥩")

filed_tag = QLineEdit()
lb_tags = QLabel('Список Тегів (～￣▽￣)～🥂')
lst_tags = QListWidget()


# нижні кнопочки
btn_tag_add = QPushButton("Додати тег ◑﹏◐☕")
btn_tag_del = QPushButton("Відкріпити від замітки (✿◕‿◕✿)🥞")
btn_tag_search = QPushButton("Шукати замітки за тегом (★ ω ★)🍕")

#штуки для паролю
#set_password = QPushButton("Встановити Пароль(ﾉ*ФωФ)ﾉ")



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


btn_tag_add.setStyleSheet('''
                        background-color: Khaki;
                        color: LightCoral;
                        font-size: 20px;
                        border: 2px solid LightGoldenRodYellow; 
                        ''')

btn_tag_del.setStyleSheet('''
                        background-color: Green;
                        color: IndianRed;
                        font-size: 20px;
                        border: 2px solid DarkSlateGrey; 
                        ''')

btn_tag_search.setStyleSheet('''
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
col2.addWidget(btn_tag_add)
col2.addWidget(btn_tag_del)
col2.addWidget(btn_tag_search)

def show_notes():
    key = lst_notes.currentItem().text()
    if 'пароль' in notes[key]:
        enter_password()
    else:
        filed_text.setText(notes[key]['текст'])
        lst_tags.clear()
        lst_tags.addItems(notes[key]['теги'])
        

    
def set_password():
    current_item = lst_notes.currentItem()
    if current_item:
        key = current_item.text()
        password, ok = QInputDialog.getText(window, 'Встановити пароль(❤ ω ❤)', 'Введіть пароль для замітки(⓿_⓿):')
        if ok:
            notes[key]['пароль'] = password
            saveToFile()
    else:
        QMessageBox.warning(window, 'Помилка(　o=^•ェ•)o　┏━┓', 'Будь ласка, виберіть замітку для встановлення паролю(。・ω・。)')


def enter_password():
    key = lst_notes.currentItem().text()
    password, ok = QInputDialog.getText(window, 'Введіть пароль(o|o) ', 'Будь ласка, введіть пароль(。・ω・。):')      
    if ok and notes[key].get('пароль') == password:
        filed_text.setText(notes[key]['текст'])
        lst_tags.clear()
        lst_tags.addItems(notes[key]['теги'])
    elif ok:
        filed_text.clear()
        filed_tag.clear()
        QMessageBox.warning(window, 'Помилка(　o=^•ェ•)o　┏━┓', 'Неправильний пароль!(。・ω・。)')

        saveToFile()

def note_create():
    note_name, ok = QInputDialog.getText(window, 'Додати Замітку', 'Нова замітка')
    if note_name and ok:
        lst_notes.addItem(note_name)
        notes[note_name] = {'текст': "", 'теги': [], 'пароль': ""}
        saveToFile()
        
def note_delete():
    if lst_notes.currentItem():
        key = lst_notes.currentItem().text()
        del notes[key]

        filed_text.clear()
        lst_tags.clear()
        lst_notes.clear()
        lst_notes.addItems(notes)

        saveToFile()

    else:
        print("Неможна")

def note_save():
    if lst_notes.currentItem():
        key = lst_notes.currentItem().text()
        notes[key]['текст'] = filed_text.toPlainText()

        saveToFile()

def tag_add():
    key = lst_notes.currentItem().text()
    tag = filed_tag.text()

    notes[key]['теги'].append(tag)

    lst_tags.addItem(tag)
    saveToFile()

    
def tag_del():
    key =lst_notes.currentItem().text()
    tag = lst_tags.currentItem().text()

    notes[key]['теги'].remove(tag)

    lst_tags.clear()
    lst_tags.addItems(notes[key]['теги'])

    saveToFile()


def tag_search():
    tag = filed_tag.text()

    if 'Шукати замітки за тегом (★ ω ★)🍕' == btn_tag_search.text():
        filtered_notes = {}

        for key in notes:
            if tag in notes[key]['теги']:
                filtered_notes[key] = notes[key]

        btn_tag_search.setText('Скинути пошук(⓿_⓿)🍳')

        lst_notes.clear()
        lst_notes.addItems(filtered_notes)
        lst_tags.clear()
        filed_text.clear()
        filed_tag.clear()

    elif  'Скинути пошук(⓿_⓿)🍳' == btn_tag_search.text():
        btn_tag_search.setText('Шукати замітки за тегом (★ ω ★)🍕')
        
        lst_notes.clear()
        lst_notes.addItems(notes)
        lst_tags.clear()
        filed_text.clear()
        filed_tag.clear()


btn_note_save.clicked.connect(note_save)
btn_note_delete.clicked.connect(note_delete)
btn_note_create.clicked.connect(note_create)
btn_note_create.clicked.connect(set_password)
lst_notes.itemClicked.connect(show_notes)

btn_tag_add.clicked.connect(tag_add)
btn_tag_del.clicked.connect(tag_del)
btn_tag_search.clicked.connect(tag_search)



with open('note.json', 'r' , encoding = 'utf8') as file:
    notes = json.load(file)

lst_notes.addItems(notes)    

window.setLayout(loyout_notes)
window.show()
app.exec()