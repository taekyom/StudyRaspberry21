#QT Designer 연동소스
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./ui/mainWindow01.ui', self)

        #UI에 있는 위젯과 연결하는 signal 처리(컨트롤 이벤트 처리)
        self.BtnStart.clicked.connect(self.BtnStart_Clicked)
        self.BtnStop.clicked.connect(self.BtnStop_Clicked)
    def BtnStart_Clicked(self):
        print('시작했습니다!')
        self.lblResult.setText('시작했습니다!')
    def BtnStop_Clicked(self):
        print('종료했습니다!')
        self.lblResult.setText('종료했습니다!')  


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
