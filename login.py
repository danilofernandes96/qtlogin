# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(764, 327)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(0, 0, 361, 331))
        self.widget.setStyleSheet("background-color: #ff7632;")
        self.widget.setObjectName("widget")

        #carrega a logo
        self.lblLogo = QtWidgets.QLabel(self.widget)
        self.lblLogo.setGeometry(QtCore.QRect(40, 40, 256, 256))
        self.lblLogo.setText("")
        self.lblLogo.setObjectName("lblLogo")
        self.lblLogo.setPixmap(QtGui.QPixmap('logo.png'))

        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(360, 0, 411, 331))
        self.widget_2.setStyleSheet("background-color: rgb(5, 55, 120);")
        self.widget_2.setObjectName("widget_2")

        self.txtUser = QtWidgets.QLineEdit(self.widget_2)
        self.txtUser.setGeometry(QtCore.QRect(120, 80, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtUser.setFont(font)
        self.txtUser.setStyleSheet("color: rgb(255, 255, 255);")
        self.txtUser.setObjectName("txtUser")

        #senha
        self.txtPw = QtWidgets.QLineEdit(self.widget_2)
        self.txtPw.setGeometry(QtCore.QRect(120, 150, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtPw.setFont(font)
        self.txtPw.setStyleSheet("color: rgb(255, 255, 255);")
        self.txtPw.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txtPw.setInputMask("")
        self.txtPw.setObjectName("txtPw")
        self.txtPw.setEchoMode(QtWidgets.QLineEdit.Password)

        #label usuário
        self.lblUser = QtWidgets.QLabel(self.widget_2)
        self.lblUser.setGeometry(QtCore.QRect(65, 70, 51, 41))
        self.lblUser.setText("")
        self.lblUser.setObjectName("lblUser")
        self.lblUser.setPixmap(QtGui.QPixmap('user.png'))

        self.lblPw = QtWidgets.QLabel(self.widget_2)
        self.lblPw.setGeometry(QtCore.QRect(65, 140, 51, 41))
        self.lblPw.setText("")
        self.lblPw.setObjectName("lblPw")
        self.lblPw.setPixmap(QtGui.QPixmap('lock.png'))

        self.btnEntrar = QtWidgets.QPushButton(self.widget_2)
        self.btnEntrar.setGeometry(QtCore.QRect(120, 220, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnEntrar.setFont(font)
        self.btnEntrar.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.267, y1:0.335, x2:0, y2:0, stop:0.00568182 rgba(0, 79, 19, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: rgb(8, 147, 31);")
        self.btnEntrar.setObjectName("btnEntrar")
        self.btnEntrar.clicked.connect(self.verificar)

        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(280, 220, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login - Tucumã Telecom"))
        self.btnEntrar.setText(_translate("MainWindow", "Entrar"))
        self.pushButton.setText(_translate("MainWindow", "Sair"))
    
    def verificar(self):
        if self.txtUser.text() == 'danilo' and self.txtPw.text() == '123':
            print('Login Aprovado')
        else:
            print('Usuário ou senha incorretos')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
