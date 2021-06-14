import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Xing_ui import *
import win32com.client 
import pythoncom 


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
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

        # - 박스 레이아웃 설절 시            
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


    # - 그리드 레이아웃으로 할 때 self 사용
        # self.ConnectServer = QLabel()
        # self.ConnectServer.resize(60, 40) 
        # self.ConnectServer.setObjectName("ConnectServer")
        # self.ConnectServer.setFont(font)
        # self.ConnectServer.setText('접속서버')

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

        layout.addLayout(hbox)
        layout.addLayout(h2box)
        layout.addLayout(h3box)
        layout.addLayout(h4box)
        # layout.addStretch(1)
        layout.addLayout(subLayout)
        self.setLayout(layout)


   
        
    def onOKButtonClicked(self):
       self.accept()



    def onCancelButtonClicked(self):
        self.reject()

    def showModal(self):
        return super().exec_()