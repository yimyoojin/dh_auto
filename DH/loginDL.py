# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginDL.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(400, 304)

        self.buttonBox = QtWidgets.QDialogButtonBox(LoginDialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 101, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.label = QtWidgets.QLabel(LoginDialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.comboBox = QtWidgets.QComboBox(LoginDialog)
        self.comboBox.setGeometry(QtCore.QRect(130, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.label_2 = QtWidgets.QLabel(LoginDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(LoginDialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 60, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")

        self.label_3 = QtWidgets.QLabel(LoginDialog)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.lineEdit_2 = QtWidgets.QLineEdit(LoginDialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 100, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.label_4 = QtWidgets.QLabel(LoginDialog)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(LoginDialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 140, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(LoginDialog)
        self.buttonBox.accepted.connect(LoginDialog.accept)
        self.buttonBox.rejected.connect(LoginDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "로그인"))
        self.label.setText(_translate("LoginDialog", "접속서버"))
        self.comboBox.setItemText(0, _translate("LoginDialog", "실서버"))
        self.comboBox.setItemText(1, _translate("LoginDialog", "모의투자"))
        self.label_2.setText(_translate("LoginDialog", "아이디"))
        self.label_3.setText(_translate("LoginDialog", "비밀번호"))
        self.label_4.setText(_translate("LoginDialog", "공인인증 암호"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginDialog = QtWidgets.QDialog()
    ui = Ui_LoginDialog()
    ui.setupUi(LoginDialog)
    LoginDialog.show()
    sys.exit(app.exec_())
