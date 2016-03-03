from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from ui import Ui_MainWindow
import sys
import os
import random
import time


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.label.setText('Pros')
        self.label_2.setText('Cons')
        self.pushButton.clicked.connect(self.do)

    def do(self):
        self.listWidget.clear()
        self.listWidget_2.clear()
        path = os.path.join(os.getcwd(), 'namelist.txt')
        try:
            people_num = self.spinBox.value()
            with open(path, 'r') as file:
                namelist = file.readlines()
            if people_num * 2 > len(namelist):
                raise ValueError
            while self.listWidget.count() is not people_num:
                name = random.choice(namelist)
                if not self.listWidget.findItems(name, Qt.MatchExactly) and not self.listWidget_2.findItems(name,Qt.MatchExactly):
                    self.listWidget.addItem(name)
            while self.listWidget_2.count() is not people_num:
                name = random.choice(namelist)
                if not self.listWidget.findItems(name, Qt.MatchExactly) and not self.listWidget_2.findItems(name,Qt.MatchExactly):
                    self.listWidget_2.addItem(name)
        except FileNotFoundError as e:
            self.statusBar.showMessage(str(e))
        except ValueError as e:
            self.statusBar.showMessage('Too many people required')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
