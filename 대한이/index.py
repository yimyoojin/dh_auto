import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Xing_ui import *
from index_2 import LoginDialog


class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.form_widget = FormWidget(self)
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(self.form_widget)
        self.setCentralWidget(widget)
        self.setupUi()
        self.center()
        

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setupUi(self):
        # 윈도우 설정
        self.setGeometry(QRect(350, 120, 1320, 800)) # x, y, w, h
        self.setWindowTitle('대한이 ver.1')

class FormWidget(QWidget):

    def __init__(self, parent):
        super(FormWidget, self).__init__(parent)
        self.__controls()
        self.__layout()
        

    def __controls(self):
        self.groupBox_1 = QGroupBox()
        self.groupBox_1.setGeometry(QRect(5, 5, 1400, 270))
        self.groupBox_1.setObjectName("groupBox_1")

        self.groupBox_2 = QGroupBox()
        self.groupBox_2.setGeometry(QRect(5, 5, 1400, 270))
        self.groupBox_2.setObjectName("groupBox_2")
        
        font = QFont()
        font.setPointSize(11)

        self.LoginButton = QPushButton(self.groupBox_1)
        self.LoginButton.setFont(font)
        self.LoginButton.setText('로그인')
        self.LoginButton.setGeometry(QRect(1183, 1, 100, 35))
        self.LoginButton.setLayoutDirection(Qt.LeftToRight)
        self.LoginButton.clicked.connect(self.onButtonClicked)

        self.Account = QLabel(self.groupBox_1)
        self.Account.setFont(font)
        self.Account.setText('계좌정보')
        self.Account.setGeometry(QRect(240, 10, 60, 25))
        self.Account.setAlignment(Qt.AlignCenter)
        

        self.Account_SelectBox = QComboBox(self.groupBox_1)
        self.Account_SelectBox.setGeometry(QRect(310, 10, 135, 25))
        self.Account_SelectBox.setObjectName("Account_SelectBox")


        self.tabWidget = QTabWidget(self.groupBox_1)
        self.tabWidget.setGeometry(QRect(5, 50, 1277, 325))
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        
        
        self.tab = QWidget()
        self.tab.setObjectName("매수")
        self.label = QLabel(self.tab)
        self.label.setObjectName("label")

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("매도")

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_49 = QLabel(self.tab_3)

        

    def __layout(self):
        # 그룹박스 레이아웃 설정
        self.groupBox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.h2Box = QHBoxLayout()
        
        self.hbox.addWidget(self.groupBox_1)
        self.h2Box.addWidget(self.groupBox_2)
        
        self.groupBox.addLayout(self.hbox)
        self.groupBox.addLayout(self.h2Box)
        self.setLayout(self.groupBox)
        

    def onButtonClicked(self):
        win = LoginDialog()
        r = win.showModal()



def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()

if __name__ == '__main__':
    sys.exit(main()) 