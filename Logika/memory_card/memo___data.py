from PyQt5.QtCore import QAbstractListModel, QModelIndex, QtMsgType
from random import randint, shuffle


class Question():
    def __init__(self, question, answear, wrong_answear1, wrong_answear2, wrong_answear3):
            self.question = question
            self.answear = answear
            self.wrong_answear1 = wrong_answear1
            self.wrong_answear2 = wrong_answear2
            self.wrong_answear3 = wrong_answear3

def got_right(self):
    print('Це правильна відповідь')

def got_wrong(self):
    print('Відповідь невірна')


class QuestionView():
    def __init__(self, frm_model, question, answear, wrong_answear1, wrong_answear2, wrong_answear3):
        self.frm_model = frm_model
        self.question = question
        self.answear = answear
        self.wrong_answear1 = wrong_answear1
        self.wrong_answear2 = wrong_answear2
        self.wrong_answear3 = wrong_answear3

    def change(self):
         pass

    def show(self):
        self.question.setText(self.frm_model.question)
        self.answear.setText(self.frm_model.answear)
        self.wrong_answear1.setText(self.frm_model.wrong_answear1)
        self.wrong_answear2.setText(self.frm_model.wrong_answear2)
        self.wrong_answear3.setText(self.frm_model.wrong_answear3)
