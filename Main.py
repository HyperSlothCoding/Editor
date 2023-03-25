from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QPushButton, QWidget
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 500, 300)
        self.setWindowTitle("Applicatoin")
        self.initUi()

    def initUi(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Application Label")
        self.label.move(210,5)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Start")
        self.b1.move(10,25)
        self.b1.clicked.connect(self.clicked)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Save")
        self.b2.move(10,60)
        self.b2.clicked.connect(self.Save)

        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("Quit")
        self.b3.move(10,95)
        self.b3.clicked.connect(self.dialog)
    
    def Save(self):
        self.GameSave = QMessageBox()

        self.GameSave.setText("Are you sure you want to save?")
        self.GameSave.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel)

        self.GameSave.exec_()

    def dialog(self):
        self.mbox = QMessageBox()

        self.mbox.setText("Are You Sure You Want To Quit?")
        self.mbox.setDetailedText("Youre Last Save was at 3:54pm")
        self.mbox.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
            
        self.mbox.exec_()

    def clicked(self):
        self.label.setText("The Game Has Started!")
        self.update()

    def update(self):
        self.label.adjustSize()



def clicked():
    print("clicked")


def Window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
Window()
