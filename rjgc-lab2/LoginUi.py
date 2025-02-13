# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(340, 130, 371, 371))
        self.frame_2.setStyleSheet("#frame_2{\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-right-radius:30px;\n"
"border-bottom-right-radius:30px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(320, 10, 51, 16))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    padding-bottom:5px;\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/1jpg.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(30, 20, 301, 331))
        self.frame_3.setMinimumSize(QtCore.QSize(301, 331))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame_6)
        self.stackedWidget_2.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton{\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_login)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_L_account = QtWidgets.QLineEdit(self.page_login)
        self.lineEdit_L_account.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_L_account.setObjectName("lineEdit_L_account")
        self.verticalLayout_4.addWidget(self.lineEdit_L_account)
        self.lineEdit_L_password = QtWidgets.QLineEdit(self.page_login)
        self.lineEdit_L_password.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_L_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_L_password.setObjectName("lineEdit_L_password")
        self.verticalLayout_4.addWidget(self.lineEdit_L_password)
        self.pushButton_L_sure = QtWidgets.QPushButton(self.page_login)
        self.pushButton_L_sure.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_L_sure.setObjectName("pushButton_L_sure")
        self.verticalLayout_4.addWidget(self.pushButton_L_sure)
        self.stackedWidget_2.addWidget(self.page_login)
        self.page_register = QtWidgets.QWidget()
        self.page_register.setObjectName("page_register")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_register)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_R_account = QtWidgets.QLineEdit(self.page_register)
        self.lineEdit_R_account.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_R_account.setText("")
        self.lineEdit_R_account.setObjectName("lineEdit_R_account")
        self.verticalLayout_5.addWidget(self.lineEdit_R_account)
        self.lineEdit_R_password1 = QtWidgets.QLineEdit(self.page_register)
        self.lineEdit_R_password1.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_R_password1.setText("")
        self.lineEdit_R_password1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_R_password1.setObjectName("lineEdit_R_password1")
        self.verticalLayout_5.addWidget(self.lineEdit_R_password1)
        self.lineEdit_R_password2 = QtWidgets.QLineEdit(self.page_register)
        self.lineEdit_R_password2.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_R_password2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_R_password2.setObjectName("lineEdit_R_password2")
        self.verticalLayout_5.addWidget(self.lineEdit_R_password2)
        self.pushButton_R_sure = QtWidgets.QPushButton(self.page_register)
        self.pushButton_R_sure.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_R_sure.setObjectName("pushButton_R_sure")
        self.verticalLayout_5.addWidget(self.pushButton_R_sure)
        self.stackedWidget_2.addWidget(self.page_register)
        self.verticalLayout_3.addWidget(self.stackedWidget_2)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet("\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_Login = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_Login.setObjectName("pushButton_Login")
        self.horizontalLayout_2.addWidget(self.pushButton_Login)
        self.pushButton_Register = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_Register.setObjectName("pushButton_Register")
        self.horizontalLayout_2.addWidget(self.pushButton_Register)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(80, 10, 141, 21))
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 110, 291, 411))
        self.frame.setStyleSheet("#frame{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.493, y2:1, stop:0 rgba(23, 0, 213, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:30px\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 70, 191, 131))
        self.label.setStyleSheet("color: rgb(167, 116, 255);\n"
"font: 75 9pt \"Agency FB\";\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Adobe Devanagari\";")
        self.label.setObjectName("label")
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        self.stackedWidget_2.setCurrentIndex(0)
        self.pushButton.clicked.connect(LoginWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.lineEdit_L_account.setPlaceholderText(_translate("LoginWindow", "账号："))
        self.lineEdit_L_password.setPlaceholderText(_translate("LoginWindow", "密码："))
        self.pushButton_L_sure.setText(_translate("LoginWindow", "确认"))
        self.lineEdit_R_account.setPlaceholderText(_translate("LoginWindow", "账号："))
        self.lineEdit_R_password1.setPlaceholderText(_translate("LoginWindow", "密码："))
        self.lineEdit_R_password2.setPlaceholderText(_translate("LoginWindow", "确认密码："))
        self.pushButton_R_sure.setText(_translate("LoginWindow", "注册"))
        self.pushButton_Login.setText(_translate("LoginWindow", "登录"))
        self.pushButton_Register.setText(_translate("LoginWindow", "注册"))
        self.label_2.setText(_translate("LoginWindow", "账号或密码错误！"))
        self.label.setText(_translate("LoginWindow", "欢迎来到\n"
"财务管理系统"))
import res_rc
