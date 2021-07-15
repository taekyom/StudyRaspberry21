#QT Designer 연동소스
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from naverSearch import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./ui/NaverSearch.ui', self)

        #UI에 있는 위젯과 연결하는 signal 처리(컨트롤 이벤트 처리)
        self.btnSearch.clicked.connect(self.btnSearch_Clicked)

    def btnSearch_Clicked(self):
        api = naverSearch()
        jsonResult = []
        sNode = 'news'
        search_word = self.txtSearchWord.text()
        display = 100

        #naver api search
        jsonSearch = api.getNaverSearchResult(sNode, search_word, 1, 100)
        print(jsonSearch)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
