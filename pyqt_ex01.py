#pyqt5로 winform 만들기(베이스 프레임 소스)
import sys
from PyQt5.QtWidgets import * # * : all

app = QApplication(sys.argv) #new와 같음
win = QWidget()
win.show()

app.exec_()
