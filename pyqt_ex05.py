#QT Designer 연동소스
import webbrowser
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
        self.tblResult.itemSelectionChanged.connect(self.tblResult_Selected)
        self.txtSearchWord.returnPressed.connect(self.btnSearch_Clicked)

    def tblResult_Selected(self):
        selected = self.tblResult.currentRow() #현재 선택된 열의 인덱스
        url = self.tblResult.item(selected, 1).text()
        QMessageBox.about(self, 'popup', '웹브라우저를 실행합니다.') #기사제목 클릭 시 발생하는 팝업
        webbrowser.open(url)
        
    def makeTable(self, result):
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblResult.setColumnCount(2)
        self.tblResult.setRowCount(len(result))
        self.tblResult.setHorizontalHeaderLabels(['기사제목', '뉴스링크'])

        n = 0
        for post in result:
            title = post['title'].replace('&lt;', '<').replace('&gt;', '>').replace('<b>', '').replace('</b>', '').replace('&quot;', "'")
            self.tblResult.setItem(n, 0, QTableWidgetItem(title))
            self.tblResult.setItem(n, 1, QTableWidgetItem(post['originallink']))
            n += 1

        self.tblResult.setColumnWidth(0, 400)    
        self.tblResult.setColumnWidth(1, 300)    
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers) #테이블 뷰에 있는 내용 수정 못하도록 막음 = readonly
        

    def btnSearch_Clicked(self):
        api = naverSearch()
        jsonResult = []
        sNode = 'news'
        search_word = self.txtSearchWord.text()
        display = 100

        #검색어를 입력하지 않고 검색버튼을 누를 때
        if len(search_word) == 0: 
            QMessageBox.about(self, 'popup', '검색어를 입력하세요!')
            return 

        #naver api search
        jsonSearch = api.getNaverSearchResult(sNode, search_word, 1, display)
        jsonResult = jsonSearch['items'] #items 리스트 분리
        print(len(jsonResult))
        self.stsResult.showMessage('검색결과 : {0}개'.format(len(jsonResult)))
        #print(jsonSearch)
        # model = QtGui.QStandardItemModel()
        # self.lsvResult.setModel(model)

        # for post in jsonSearch['items']:
        #     item = QtGui.QStandardItem(post['title'])
        #     model.appendRow(item)
        self.makeTable(jsonResult)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
