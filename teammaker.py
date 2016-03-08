from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui import Ui_MainWindow
import sys
import os
import random


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.do)
        self.pushButton_2.clicked.connect(self.get_file_path)

    def get_file_path(self):
        self.file_path=QFileDialog.getOpenFileName(self,'Open File',os.getcwd())[0]

    def do(self):
        self.listWidget.clear()
        self.listWidget_2.clear()
        if hasattr(self,'file_path') is False:
            self.file_path = os.path.join(os.getcwd(), 'namelist.txt')
        try:
            people_num = self.spinBox.value()
            with open(self.file_path, 'r') as file:
                namelist = file.readlines()
            if people_num * 2 > len(namelist):
                raise ValueError
            random.shuffle(namelist)
            namelist = namelist[:people_num * 2]
            for i in range(len(namelist)):
                namelist[i] = namelist[i].replace('\n', '')
            self.listWidget.addItems(namelist[:people_num])
            self.listWidget_2.addItems(namelist[people_num:])
        except FileNotFoundError as e:
            self.statusBar.showMessage(str(e))
        except ValueError as e:
            self.statusBar.showMessage('Too many people required')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
