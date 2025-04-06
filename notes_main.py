def add_note():
    note_name, ok = QInputDialog.getText(win, 'Добавить заметку', 'Название заметки:')
    if ok and note_name != "":
        data[note_name] = {'текст' : "", "теги" : []}
        notesList.addItem(note_name)
        tagsList.addItems(data[note_name]['теги'])

def show_note():
    key = notesList.selectedItems()[0].text()
    textEdit.setText(data[key]['текст'])
    tagsList.clear()
    tagsList.addItems(data[key]['теги'])

def save_note():
    if notesList.selectedItems():
        key = notesList.selectedItems()[0].text()
        data[key]['текст'] = textEdit.toPlainText()
        with open('Data.json', 'w') as file:
            json.dump(data, file, sort_keys=True)
    else:
        pass

def del_note():
    if notesList.selectedItems():
        key = notesList.selectedItems()[0].text()
        del data[key]
        notesList.clear()
        tagsList.clear()
        textEdit.clear()
        notesList.addItems(data)
        with open('Data.json', 'w') as file:
            json.dump(data, file, sort_keys=True)
    else:
        pass

def add_tag():
    if notesList.selectedItems():
        key = notesList.selectedItems()[0].text()
        tag = lineEdit.text()
        if not tag in data[key]['теги']:
            data[key]['теги'].append(tag)
            tagsList.addItem(tag)
            lineEdit.clear()
        with open('Data.json', 'w') as file:
            json.dump(data, file, sort_keys=True)
    else:
        pass




import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QVBoxLayout, QHBoxLayout, QPushButton,
    QListWidget, QLineEdit, QTextEdit, QInputDialog)

app = QApplication([])
win = QWidget()
win.setWindowTitle('Умные заметки')
win.resize(800, 600)

textEdit = QTextEdit()
notesList =  QListWidget()
tagsList = QListWidget()
lineEdit = QLineEdit()
add_note_btn = QPushButton('создать заметку')
del_note_btn = QPushButton('удалить заметку')
save_note_btn = QPushButton('сохранить заметку')
add_tag_btn = QPushButton('создать тег')
del_tag_btn = QPushButton('удалить тег')
search_tag_btn = QPushButton('искать по тег')

mainLine = QHBoxLayout()
leftLine = QVBoxLayout()
rightLine = QVBoxLayout()
Line1 = QHBoxLayout()
Line2 = QHBoxLayout()
Line3 = QHBoxLayout()
Line4 = QHBoxLayout()
Line5 = QHBoxLayout()
Line6 = QHBoxLayout()
Line7 = QHBoxLayout()

Line1.addWidget(notesList)
Line2.addWidget(add_note_btn)
Line2.addWidget(del_note_btn)
Line3.addWidget(save_note_btn)
Line4.addWidget(tagsList)
Line5.addWidget(lineEdit)
Line6.addWidget(add_tag_btn)
Line6.addWidget(del_tag_btn)
Line7.addWidget(search_tag_btn)

rightLine.addLayout(Line1)
rightLine.addLayout(Line2)
rightLine.addLayout(Line3)
rightLine.addLayout(Line4)
rightLine.addLayout(Line5)
rightLine.addLayout(Line6)
rightLine.addLayout(Line7)

leftLine.addWidget(textEdit)

mainLine.addLayout(leftLine)
mainLine.addLayout(rightLine)

win.setLayout(mainLine)

add_note_btn.clicked.connect(add_note)
notesList.itemClicked.connect(show_note)
save_note_btn.clicked.connect(save_note)
del_note_btn.clicked.connect(del_note)
add_tag_btn.clicked.connect(add_tag)
#del_tag_btn.clicked.connect(del_tag)



with open('Data.json', 'r') as file:
    data = json.load(file)
notesList.addItems(data)

win.show()
app.exec_()


