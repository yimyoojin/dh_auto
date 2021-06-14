import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Xing_ui import *
# from loginDL import LoginDialog


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.api = XASession()
        self.api.login_contact()
        self.initUI()
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        self.setWindowTitle('로그인')
        self.resize(400, 300) 

        font = QFont()
        font.setPointSize(11)

        # 위젯 설정 
        # - 박스 레이아웃 설정 시            
        Server = QLabel()
        Server.resize(60, 40) 
        Server.setObjectName("Server")
        Server.setFont(font)
        Server.setText('접속서버')

        comboBox = QComboBox()
        comboBox.resize(100, 40) 
        comboBox.setLayoutDirection(Qt.LeftToRight)
        comboBox.setObjectName("comboBox")
        comboBox.setFont(font)      
        comboBox.addItem("실서버")
        comboBox.addItem("모의투자")

        ID = QLabel()
        ID.resize(60, 40) 
        ID.setObjectName("ID")
        ID.setFont(font)    
        ID.setText('아이디')
        
        ID_edit = QLineEdit()
        ID_edit.resize(100, 40) 
        ID_edit.setLayoutDirection(Qt.LeftToRight)
        ID_edit.setFont(font)    
        ID_edit.setObjectName("ID_edit")
         
        PW = QLabel()
        PW.resize(60, 40) 
        PW.setObjectName("PW")
        PW.setFont(font)    
        PW.setText('비밀번호')

        PW_edit = QLineEdit()
        PW_edit.resize(100, 40) 
        PW_edit.setLayoutDirection(Qt.LeftToRight)
        PW_edit.setFont(font)    
        PW_edit.setObjectName("PW_edit")

        cert_pw = QLabel()
        cert_pw.resize(60, 40)
        cert_pw.setObjectName("cert_pw")
        cert_pw.setFont(font)
        cert_pw.setText('공인인증 암호')

        cert_pw_edit = QLineEdit()
        cert_pw_edit.resize(100, 40)
        cert_pw_edit.setLayoutDirection(Qt.LeftToRight)
        cert_pw_edit.setFont(font)
        cert_pw_edit.setObjectName("cert_pw_edit")

        btnOK = QPushButton("로그인")
        btnOK.resize(120, 50)
        btnOK.setFont(font)
        btnOK.clicked.connect(self.onOKButtonClicked)

        btnCancel = QPushButton("취소")
        btnCancel.resize(120, 50)
        btnCancel.setFont(font)
        btnCancel.clicked.connect(self.onCancelButtonClicked)

        onlogin = QLabel()
        onlogin.setFont(font)
        onlogin.api.connect(self.OnLogin)


    # - 그리드 레이아웃으로 할 때 self 사용
        # self.Server = QLabel()
        # self.Server.resize(60, 40) 
        # self.Server.setObjectName("Server")
        # self.Server.setFont(font)
        # self.Server.setText('접속서버')

        # self.comboBox = QComboBox()
        # self.comboBox.resize(100, 40) 
        # self.comboBox.setLayoutDirection(Qt.LeftToRight)
        # self.comboBox.setObjectName("comboBox")
        # self.comboBox.setFont(font)      
        # self.comboBox.addItem("실서버")
        # self.comboBox.addItem("모의투자")

        # self.ID = QLabel()
        # self.ID.resize(60, 40) 
        # self.ID.setObjectName("ID")
        # self.ID.setFont(font)    
        # self.ID.setText('아이디')

        # self.ID_edit = QLineEdit()
        # self.ID_edit.resize(100, 40) 
        # self.ID_edit.setLayoutDirection(Qt.LeftToRight)
        # self.ID_edit.setFont(font)    
        # self.ID_edit.setObjectName("ID_edit")  
 
        # self.PW = QLabel()
        # self.PW.resize(60, 40) 
        # self.PW.setObjectName("PW")
        # self.PW.setFont(font)    
        # self.PW.setText('비밀번호')

        # self.PW_edit = QLineEdit()
        # self.PW_edit.resize(100, 40) 
        # self.PW_edit.setLayoutDirection(Qt.LeftToRight)
        # self.PW_edit.setFont(font)    
        # self.PW_edit.setObjectName("PW_edit")

        # self.cert_pw = QLabel()
        # self.cert_pw.resize(60, 40)
        # self.cert_pw.setObjectName("cert_pw")
        # self.cert_pw.setFont(font)
        # self.cert_pw.setText('공인인증 암호')

        # self.cert_pw_edit = QLineEdit()
        # self.cert_pw_edit.resize(100, 40)
        # self.cert_pw_edit.setLayoutDirection(Qt.LeftToRight)
        # self.cert_pw_edit.setFont(font)
        # self.cert_pw_edit.setObjectName("cert_pw_edit")

        # self.btnOK = QPushButton("확인")
        # self.btnOK.resize(120, 50)
        # self.btnOK.setFont(font)
        # self.btnOK.clicked.connect(self.onOKButtonClicked)

        # self.btnCancel = QPushButton("취소")
        # self.btnCancel.resize(120, 50)
        # self.btnCancel.setFont(font)
        # self.btnCancel.clicked.connect(self.onCancelButtonClicked)


    # 전체 레이아웃 세팅             
        # - 박스형 레이아웃
        layout = QVBoxLayout()
        hbox = QHBoxLayout()
        h2box = QHBoxLayout()
        h3box = QHBoxLayout()
        h4box = QHBoxLayout()
        subLayout = QHBoxLayout() 
        h5box = QHBoxLayout()


        hbox.addWidget(Server, stretch=1)
        hbox.addWidget(comboBox, stretch=1)  

        h2box.addWidget(ID, stretch=1)
        h2box.addWidget(ID_edit)

        h3box.addWidget(PW, stretch=1)
        h3box.addWidget(PW_edit)
        
        h4box.addWidget(cert_pw, stretch=1)
        h4box.addWidget(cert_pw_edit)
        
        
        subLayout.addWidget(btnOK)
        subLayout.addWidget(btnCancel)

        h5box.addWidget(onlogin)

        layout.addLayout(hbox)
        layout.addLayout(h2box)
        layout.addLayout(h3box)
        layout.addLayout(h4box)
        layout.addLayout(subLayout)
        layout.addStretch(1)
        layout.addLayout(h5box)
        self.setLayout(layout)

        
    def onOKButtonClicked(self): 
        

        self.accept()

    def onCancelButtonClicked(self):
        self.reject()

    def showModal(self):
        return super().exec_()

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
        
        
        self.tab = QWidget(self.tabWidget)
        self.tab.resize(30,20)
        self.tabWidget.addTab(self.set_tabWidget(), "매수")
        self.tab.setFont(font)
        self.tab.setObjectName("tab")
        # self.tab.addWidget(self.set_tabWidget)

        self.tab_2 = QWidget(self.tabWidget)
        self.tab_2.resize(30,20)
        self.tabWidget.addTab(self.set_tabWidget(), "매도")
        self.tab_2.setFont(font)
        self.tab_2.setObjectName("tab_2")
        # self.tab_2.addWidget(self.set_tabWidget)

        self.tab_3 = QWidget(self.tabWidget)
        self.tab_3.resize(30,20)
        self.tabWidget.addTab(self.set_tabWidget(), "정정/취소")
        self.tab_3.setFont(font)
        self.tab_3.setObjectName("tab_3")
        # self.tab_3.addWidget(self.set_tabWidget)

    def set_tabWidget(self):
        font = QFont()
        font.setPointSize(11)
        
        self.label = QLabel()
        self.label.setGeometry(QRect(20, 20, 30, 20))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label.setObjectName("label")

        self.lineEdit = QLineEdit()
        self.lineEdit.setGeometry(QRect(60, 20, 110, 20))
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QLineEdit()
        self.lineEdit_2.setGeometry(QRect(60, 50, 150, 20))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton_4 = QPushButton()
        self.pushButton_4.setGeometry(QRect(180, 20, 31, 23))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../img/아이콘/화면 캡처 2021-02-25 180142.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QSize(30, 30))
        self.pushButton_4.setObjectName("pushButton_4")


        self.label_4 = QLabel()
        self.label_4.setGeometry(QRect(20, 80, 31, 21))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")

        self.comboBox_3 = QComboBox()
        self.comboBox_3.setGeometry(QRect(60, 80, 151, 22))
        self.comboBox_3.setMinimumSize(QSize(0, 22))
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("보통")
        self.comboBox_3.addItem("시장가")


        self.label_5 = QLabel()
        self.label_5.setGeometry(QRect(20, 110, 31, 21))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")

        self.spinBox_2 = QSpinBox()
        self.spinBox_2.setGeometry(QRect(60, 110, 111, 22))
        self.spinBox_2.setFont(font)
        self.spinBox_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_2.setMaximum(100000000)
        self.spinBox_2.setObjectName("spinBox_2")

        self.pushButton_2 = QPushButton()
        self.pushButton_2.setGeometry(QRect(180, 110, 31, 23))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")


        self.label_6 = QLabel()
        self.label_6.setGeometry(QRect(20, 140, 31, 21))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")

        self.spinBox = QSpinBox()
        self.spinBox.setGeometry(QRect(60, 140, 111, 22))
        self.spinBox.setFont(font)
        self.spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox.setMaximum(1000000000)
        self.spinBox.setSingleStep(50)
        self.spinBox.setObjectName("spinBox")

        self.pushButton = QPushButton()
        self.pushButton.setGeometry(QRect(180, 140, 31, 23))
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")


        self.groupBox = QGroupBox()
        self.groupBox.setGeometry(QRect(60, 170, 151, 21))
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QRect(20, 0, 51, 21))
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QRect(90, 0, 51, 21))
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")


        self.groupBox_3 = QGroupBox()
        self.groupBox_3.setGeometry(QRect(230, 10, 1031, 151))
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")


        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setGeometry(QRect(20, 30, 141, 21))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")


        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setGeometry(QRect(30, 70, 111, 21))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")

        self.lineEdit_3 = QLineEdit(self.groupBox_3)
        self.lineEdit_3.setGeometry(QRect(170, 70, 161, 20))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setGeometry(QRect(340, 70, 21, 21))
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")

        
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setGeometry(QRect(30, 100, 131, 21))
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")

        self.lineEdit_4 = QLineEdit(self.groupBox_3)
        self.lineEdit_4.setGeometry(QRect(170, 100, 161, 20))
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setGeometry(QRect(340, 100, 21, 21))
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")


        self.line = QFrame(self.groupBox_3)
        self.line.setGeometry(QRect(380, 30, 20, 101))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")


        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setGeometry(QRect(409, 20, 141, 21))
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")


        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setGeometry(QRect(430, 50, 51, 21))
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")

        self.doubleSpinBox = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox.setGeometry(QRect(511, 50, 121, 22))
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setDecimals(5)
        self.doubleSpinBox.setMinimum(-10.0)
        self.doubleSpinBox.setMaximum(-0.5)
        self.doubleSpinBox.setSingleStep(0.5)
        self.doubleSpinBox.setObjectName("doubleSpinBox")


        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setGeometry(QRect(430, 80, 51, 21))
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")

        self.spinBox_3 = QSpinBox(self.groupBox_3)
        self.spinBox_3.setGeometry(QRect(510, 80, 121, 22))
        self.spinBox_3.setFont(font)
        self.spinBox_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(10)
        self.spinBox_3.setObjectName("spinBox_3")


        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setGeometry(QRect(430, 110, 51, 21))
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")

        self.spinBox_4 = QSpinBox(self.groupBox_3)
        self.spinBox_4.setGeometry(QRect(510, 110, 121, 22))
        self.spinBox_4.setFont(font)
        self.spinBox_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(10)
        self.spinBox_4.setObjectName("spinBox_4")


        self.line_2 = QFrame(self.groupBox_3)
        self.line_2.setGeometry(QRect(660, 30, 20, 101))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")


        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setGeometry(QRect(690, 20, 171, 21))
        self.label_15.setFont(font)
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")


        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setGeometry(QRect(700, 50, 51, 21))
        self.label_16.setFont(font)
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")

        
        self.lineEdit_5 = QLineEdit(self.groupBox_3)
        self.lineEdit_5.setGeometry(QRect(750, 50, 111, 20))
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.comboBox_2 = QComboBox(self.groupBox_3)
        self.comboBox_2.setGeometry(QRect(890, 50, 51, 22))
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2%")
        self.comboBox_2.addItem("0%")
        self.comboBox_2.addItem("10%")
        self.comboBox_2.addItem("20%")
        self.comboBox_2.addItem("30%")
        self.comboBox_2.addItem("40%")
        self.comboBox_2.addItem("50%")
        self.comboBox_2.addItem("60%")
        self.comboBox_2.addItem("70%")
        self.comboBox_2.addItem("80%")
        self.comboBox_2.addItem("90%")
        self.comboBox_2.addItem("100%")


        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setGeometry(QRect(700, 80, 51, 21))
        self.label_17.setFont(font)
        self.label_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")

        self.lineEdit_7 = QLineEdit(self.groupBox_3)
        self.lineEdit_7.setGeometry(QRect(750, 80, 111, 20))
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setAlignment(Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.lineEdit_11 = QLineEdit(self.groupBox_3)
        self.lineEdit_11.setGeometry(QRect(890, 80, 51, 20))
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_11.setObjectName("lineEdit_11%")


        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setGeometry(QRect(700, 110, 51, 21))
        self.label_18.setFont(font)
        self.label_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")

        self.lineEdit_6 = QLineEdit(self.groupBox_3)
        self.lineEdit_6.setGeometry(QRect(750, 110, 111, 20))
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")


        self.pushButton_3 = QPushButton()
        self.pushButton_3.setGeometry(QRect(230, 170, 121, 23))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

    # self 제거 버전
        # label = QLabel()
        # label.setGeometry(QRect(20, 20, 30, 20))
        # label.setFont(font)
        # label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # label.setObjectName("label")

        # lineEdit = QLineEdit()
        # lineEdit.setGeometry(QRect(60, 20, 110, 20))
        # lineEdit.setFont(font)
        # lineEdit.setObjectName("lineEdit")

        # lineEdit_2 = QLineEdit()
        # lineEdit_2.setGeometry(QRect(60, 50, 150, 20))
        # lineEdit_2.setFont(font)
        # lineEdit_2.setStyleSheet("background-color: rgb(217, 217, 217);")
        # lineEdit_2.setObjectName("lineEdit_2")

        # pushButton_4 = QPushButton()
        # pushButton_4.setGeometry(QRect(180, 20, 31, 23))
        # pushButton_4.setFont(font)
        # pushButton_4.setText("")
        # icon1 = QtGui.QIcon()
        # icon1.addPixmap(QtGui.QPixmap("../img/아이콘/화면 캡처 2021-02-25 180142.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # pushButton_4.setIcon(icon1)
        # pushButton_4.setIconSize(QSize(30, 30))
        # pushButton_4.setObjectName("pushButton_4")


        # label_4 = QLabel()
        # label_4.setGeometry(QRect(20, 80, 31, 21))
        # label_4.setFont(font)
        # label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # label_4.setObjectName("label_4")

        # comboBox_3 = QComboBox()
        # comboBox_3.setGeometry(QRect(60, 80, 151, 22))
        # comboBox_3.setMinimumSize(QSize(0, 22))
        # comboBox_3.setFont(font)
        # comboBox_3.setObjectName("comboBox_3")
        # comboBox_3.addItem("보통")
        # comboBox_3.addItem("시장가")


        # label_5 = QLabel()
        # label_5.setGeometry(QRect(20, 110, 31, 21))
        # label_5.setFont(font)
        # label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # label_5.setObjectName("label_5")

        # spinBox_2 = QSpinBox()
        # spinBox_2.setGeometry(QRect(60, 110, 111, 22))
        # spinBox_2.setFont(font)
        # spinBox_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        # spinBox_2.setMaximum(100000000)
        # spinBox_2.setObjectName("spinBox_2")

        # pushButton_2 = QPushButton()
        # pushButton_2.setGeometry(QRect(180, 110, 31, 23))
        # pushButton_2.setFont(font)
        # pushButton_2.setObjectName("pushButton_2")


        # label_6 = QLabel()
        # label_6.setGeometry(QRect(20, 140, 31, 21))
        # label_6.setFont(font)
        # label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # label_6.setObjectName("label_6")

        # spinBox = QSpinBox()
        # spinBox.setGeometry(QRect(60, 140, 111, 22))
        # spinBox.setFont(font)
        # spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        # spinBox.setMaximum(1000000000)
        # spinBox.setSingleStep(50)
        # spinBox.setObjectName("spinBox")

        # pushButton = QPushButton()
        # pushButton.setGeometry(QRect(180, 140, 31, 23))
        # pushButton.setFont(font)
        # pushButton.setObjectName("pushButton")


        # groupBox = QGroupBox()
        # groupBox.setGeometry(QRect(60, 170, 151, 21))
        # groupBox.setFont(font)
        # groupBox.setTitle("현금_신용")
        # groupBox.setObjectName("groupBox")

        # radioButton = QRadioButton(self.groupBox)
        # radioButton.setGeometry(QRect(20, 0, 51, 21))
        # radioButton.setFont(font)
        # radioButton.setObjectName("radioButton")

        # radioButton_2 = QRadioButton(self.groupBox)
        # radioButton_2.setGeometry(QRect(90, 0, 51, 21))
        # radioButton_2.setFont(font)
        # radioButton_2.setObjectName("radioButton_2")


        # groupBox_3 = QGroupBox()
        # groupBox_3.setGeometry(QRect(230, 10, 1031, 151))
        # groupBox_3.setFont(font)
        # groupBox_3.setObjectName("groupBox_3")


        # label_3 = QLabel(self.groupBox_3)
        # label_3.setGeometry(QRect(20, 30, 141, 21))
        # label_3.setFont(font)
        # label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # label_3.setObjectName("label_3")


        # label_7 = QLabel(self.groupBox_3)
        # label_7.setGeometry(QRect(30, 70, 111, 21))
        # label_7.setFont(font)
        # label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # label_7.setObjectName("label_7")

        # lineEdit_3 = QLineEdit(self.groupBox_3)
        # lineEdit_3.setGeometry(QRect(170, 70, 161, 20))
        # lineEdit_3.setFont(font)
        # lineEdit_3.setObjectName("lineEdit_3")

        # label_9 = QLabel(self.groupBox_3)
        # label_9.setGeometry(QRect(340, 70, 21, 21))
        # label_9.setFont(font)
        # label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # label_9.setObjectName("label_9")

        
        # label_8 = QLabel(self.groupBox_3)
        # label_8.setGeometry(QRect(30, 100, 131, 21))
        # label_8.setFont(font)
        # label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # label_8.setObjectName("label_8")

        # lineEdit_4 = QLineEdit(self.groupBox_3)
        # lineEdit_4.setGeometry(QRect(170, 100, 161, 20))
        # lineEdit_4.setFont(font)
        # lineEdit_4.setObjectName("lineEdit_4")

        # label_10 = QLabel(self.groupBox_3)
        # label_10.setGeometry(QRect(340, 100, 21, 21))
        # label_10.setFont(font)
        # label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # label_10.setObjectName("label_10")


        # line = QFrame(self.groupBox_3)
        # line.setGeometry(QRect(380, 30, 20, 101))
        # line.setFrameShape(QFrame.VLine)
        # line.setFrameShadow(QFrame.Sunken)
        # line.setObjectName("line")


        # label_11 = QLabel(self.groupBox_3)
        # label_11.setGeometry(QRect(409, 20, 141, 21))
        # label_11.setFont(font)
        # label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # label_11.setObjectName("label_11")


        # label_12 = QLabel(self.groupBox_3)
        # label_12.setGeometry(QRect(430, 50, 51, 21))
        # label_12.setFont(font)
        # label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # label_12.setObjectName("label_12")

        # doubleSpinBox = QDoubleSpinBox(self.groupBox_3)
        # doubleSpinBox.setGeometry(QRect(511, 50, 121, 22))
        # doubleSpinBox.setFont(font)
        # doubleSpinBox.setDecimals(5)
        # doubleSpinBox.setMinimum(-10.0)
        # doubleSpinBox.setMaximum(-0.5)
        # doubleSpinBox.setSingleStep(0.5)
        # doubleSpinBox.setObjectName("doubleSpinBox")


        # label_13 = QLabel(self.groupBox_3)
        # label_13.setGeometry(QRect(430, 80, 51, 21))
        # label_13.setFont(font)
        # label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # label_13.setObjectName("label_13")

        # spinBox_3 = QSpinBox(self.groupBox_3)
        # spinBox_3.setGeometry(QRect(510, 80, 121, 22))
        # spinBox_3.setFont(font)
        # spinBox_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        # spinBox_3.setMinimum(1)
        # spinBox_3.setMaximum(10)
        # spinBox_3.setObjectName("spinBox_3")


        # label_14 = QLabel(self.groupBox_3)
        # label_14.setGeometry(QRect(430, 110, 51, 21))
        # label_14.setFont(font)
        # label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # label_14.setObjectName("label_14")

        # spinBox_4 = QSpinBox(self.groupBox_3)
        # spinBox_4.setGeometry(QRect(510, 110, 121, 22))
        # spinBox_4.setFont(font)
        # spinBox_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        # spinBox_4.setMinimum(1)
        # spinBox_4.setMaximum(10)
        # spinBox_4.setObjectName("spinBox_4")


        # line_2 = QFrame(self.groupBox_3)
        # line_2.setGeometry(QRect(660, 30, 20, 101))
        # line_2.setFrameShape(QFrame.VLine)
        # line_2.setFrameShadow(QFrame.Sunken)
        # line_2.setObjectName("line_2")


        # label_15 = QLabel(self.groupBox_3)
        # label_15.setGeometry(QRect(690, 20, 171, 21))
        # label_15.setFont(font)
        # label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # label_15.setObjectName("label_15")


        # label_16 = QLabel(self.groupBox_3)
        # label_16.setGeometry(QRect(700, 50, 51, 21))
        # label_16.setFont(font)
        # label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # label_16.setObjectName("label_16")

        
        # lineEdit_5 = QLineEdit(self.groupBox_3)
        # lineEdit_5.setGeometry(QRect(750, 50, 111, 20))
        # lineEdit_5.setFont(font)
        # lineEdit_5.setObjectName("lineEdit_5")

        # comboBox_2 = QComboBox(self.groupBox_3)
        # comboBox_2.setGeometry(QRect(890, 50, 51, 22))
        # comboBox_2.setFont(font)
        # comboBox_2.setObjectName("comboBox_2%")
        # comboBox_2.addItem("0%")
        # comboBox_2.addItem("10%")
        # comboBox_2.addItem("20%")
        # comboBox_2.addItem("30%")
        # comboBox_2.addItem("40%")
        # comboBox_2.addItem("50%")
        # comboBox_2.addItem("60%")
        # comboBox_2.addItem("70%")
        # comboBox_2.addItem("80%")
        # comboBox_2.addItem("90%")
        # comboBox_2.addItem("100%")


        # label_17 = QLabel(self.groupBox_3)
        # label_17.setGeometry(QRect(700, 80, 51, 21))
        # label_17.setFont(font)
        # label_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # label_17.setObjectName("label_17")

        # lineEdit_7 = QLineEdit(self.groupBox_3)
        # lineEdit_7.setGeometry(QRect(750, 80, 111, 20))
        # lineEdit_7.setFont(font)
        # lineEdit_7.setAlignment(Qt.AlignCenter)
        # lineEdit_7.setObjectName("lineEdit_7")

        # lineEdit_11 = QLineEdit(self.groupBox_3)
        # lineEdit_11.setGeometry(QRect(890, 80, 51, 20))
        # lineEdit_11.setFont(font)
        # lineEdit_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        # lineEdit_11.setObjectName("lineEdit_11%")


        # label_18 = QLabel(self.groupBox_3)
        # label_18.setGeometry(QRect(700, 110, 51, 21))
        # label_18.setFont(font)
        # label_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # label_18.setObjectName("label_18")

        # lineEdit_6 = QLineEdit(self.groupBox_3)
        # lineEdit_6.setGeometry(QRect(750, 110, 111, 20))
        # lineEdit_6.setFont(font)
        # lineEdit_6.setObjectName("lineEdit_6")


        # pushButton_3 = QPushButton()
        # pushButton_3.setGeometry(QRect(230, 170, 121, 23))
        # pushButton_3.setFont(font)
        # pushButton_3.setObjectName("pushButton_3")

    # tabwidget 레이아웃 설정
        self.tabwidget.layout = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.h2Box = QHBoxLayout()
        self.h3Box = QHBoxLayout()
        

        self.hbox.addWidget(self.label)
        self.hbox.addWidget(self.lineEdit)
        self.hbox.addWidget(self.pushButton_4)
        self.hbox.addWidget(self.groupBox_3)

        self.h2Box.addWidget(self.lineEdit_2)
        self.h2Box.addWidget(self.)


        self.h3Box.addWidget(self.)
        
        self.tabwidget.layout.addLayout(self.hbox)
        self.tabwidget.layout.addLayout(self.h2Box)
        self.setLayout(self.groupBox)




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