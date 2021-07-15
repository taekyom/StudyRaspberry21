#pyqt5로 사용자 윈도우 클래스 생성 예제
import sys
from PyQt5.QtWidgets import * # * : all

#윈도우 클래스 선언
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__() #super : 부모클래스

app = QApplication(sys.argv) #new와 같음

# button = QPushButton("Click Me")
# button.show()

# label = QLabel("Hello QT5")
# label.show()

win = MyWindow()
win.show()
app.exec_()
