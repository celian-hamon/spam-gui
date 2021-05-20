import spam
import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(330, 200))    
        self.setWindowTitle("spam du futur") 

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('texte :')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)

        self.spinLabel = QLabel(self)
        self.spinLabel.setText('reps :')
        self.spin = QSpinBox(self)
        self.spin.setValue(100)
        self.spin.setMaximum(1000)

        self.spin.move(80, 60)
        self.spin.resize(200, 32)
        self.spinLabel.move(20, 60)

        self.dial = QDial(self)
        self.dial.setValue(8)
        self.dial.setMinimum(0)
        self.dial.setMaximum(20)
        self.dial.setNotchesVisible(True)

        self.dial.move(155, 100)
        self.dial.resize(50,50)

        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80, 150)        

    def clickMethod(self):
        print([self.line.text(),self.spin.value(),self.dial.value()])
        spam.spamfct(self.line.text(),self.spin.value(),self.dial.value())
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("windows")
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )