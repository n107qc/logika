from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel, 
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget, QListWidgetItem, QFormLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json

app = QApplication([])
window = QWidget()
main_width, main_height = 800, 600  #  розміри головного вікна

text_editor = QTextEdit()
text_editor.setPlaceholderText('Введіть текст...')

list_widget_1 = QListWidget()
list_widget_2 = QListWidget()
input_dialog = QLineEdit()
input_dialog.setPlaceholderText('Введіть тег...')

# верхні кнопочки
btn_note_create = QPushButton()
btn_note_create.setText('Створити заміточку')
btn_note_delete = QPushButton()
btn_note_delete.setText('Видалити заміточку')
btn_note_save = QPushButton()
btn_note_save.setText('Зберегти заміточку')


# нижні кнопочки
btn_note_add_notes = QPushButton()
btn_note_add_notes.setText('Додати до заміточок')
btn_note_unpin = QPushButton()
btn_note_unpin.setText('Відкріпити від заміточок')
btn_note_search_teg = QPushButton()
btn_note_search_teg.setText('Шукати заміточку за тегом')




row2 = QHBoxLayout()
row2.addWidget(btn_note_add_notes)
row2.addWidget(btn_note_unpin)
row1 = QHBoxLayout()
row1.addWidget(btn_note_create)
row1.addWidget(btn_note_delete)

col1 = QVBoxLayout()
col1.addWidget(text_editor)

col2 = QVBoxLayout()
col2.addWidget(QLabel('Список заміточок'))
col2.addWidget(list_widget_1)
col2.addLayout(row1) 
col2.addWidget(btn_note_save)  
col2.addWidget(QLabel('Список тегів'))
col2.addWidget(list_widget_2)
col2.addWidget(input_dialog)
col2.addLayout(row2)
col2.addWidget(btn_note_search_teg)

layout_notes = QHBoxLayout()
layout_notes.addLayout(col1, stretch=2)
layout_notes.addLayout(col2)


with open('note.json', 'r', encoding='utf8') as file:
    notes = json.load(file)

list_widget_1.addItems(notes)





window.setLayout(layout_notes)
window.resize(main_width,main_height)
window.show()
app.exec_()