from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, 
    QHBoxLayout, QVBoxLayout, QListWidget, QLineEdit, 
    QTextEdit, QInputDialog, QTableWidget,  QListWidgetItem,
    QFormLayout, QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json

app = QApplication([])

window = QWidget()




filed_text = QTextEdit()
lb_notes = QLabel("Список Заміток")
lst_notes = QListWidget()


btn_note_create = QPushButton("Створити")
btn_note_delete = QPushButton("Видалити")
btn_note_save = QPushButton("Зберигти")

lb_tags = QLabel('Список Тегів')
list_tags = QListWidget()


btn_note_add_notes = QPushButton("Додати до замітки")
btn_note_unpin = QPushButton("Відкріпити від замітки")
btn_note_search_teg = QPushButton("Шукати замітки за тегом")

loyout_notes = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

loyout_notes.addLayout(col1)
loyout_notes.addLayout(col2)
col1.addWidget(filed_text)
col2.addWidget(lb_notes)
col2.addWidget(lst_notes)
col2.addWidget(btn_note_create)
col2.addWidget(btn_note_unpin)
col2.addWidget(btn_note_search_teg)

row1 = QHBoxLayout()
row1.addWidget(btn_note_create)
row1.addWidget(btn_note_delete)
row1.addWidget(btn_note_save)

row2 = QVBoxLayout()
row2.addWidget(btn_note_add_notes)
row2.addWidget(btn_note_unpin)
row2.addWidget(btn_note_search_teg)

with open('note.json', 'r' , encoding = 'utf8') as file:
    notes = json.load(file)

lst_notes.addItems(notes)    


window.setLayout(loyout_notes)
window.show()
app.exec()
