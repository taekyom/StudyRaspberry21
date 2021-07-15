#pyqt5로 사용자 윈도우 구성 예제
import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import * # * : all

#윈도우 클래스 선언
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__() #super : 부모클래스

        self.setWindowTitle('My QT5 Window') #제목표시줄
        self.setGeometry(500, 200, 800, 600) # x, y, width, height
        self.setWindowIcon(QIcon('./image/chart.png')) #아이콘

        #label 추가
        self.label = QLabel('메시지 : ', self)
        self.label.move(10, 10)
        self.label.setFixedSize(QSize(300, 20))
        self.label.setGeometry(10, 10, 300, 20)

        #button 추가
        self.btn = QPushButton('Click', self)
        self.btn.move(10, 50)

        #signal 추가
        self.btn.clicked.connect(self.btn_clicked)
    
    #button click signal(event)
    def btn_clicked(self):
        self.label.clear()
        self.label.setText('메시지 : 버튼클릭!')

        
app = QApplication(sys.argv) #new와 같음
win = MyWindow()
win.show()
app.exec_()
