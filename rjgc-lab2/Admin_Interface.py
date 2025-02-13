# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin_Interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        AdminWindow.setObjectName("AdminWindow")
        AdminWindow.resize(1020, 695)
        self.centralwidget = QtWidgets.QWidget(AdminWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(110, 40, 861, 591))
        self.frame.setMinimumSize(QtCore.QSize(861, 591))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setToolTipDuration(0)
        self.frame_6.setStyleSheet("Qframe{\n"
"  border:none;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setGeometry(QtCore.QRect(80, 10, 131, 41))
        self.label.setStyleSheet("font: 15pt \"Algerian\";\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 20, 31, 31))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}")
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/OIP-C.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setStyleSheet("Qframe{\n"
"  border:none;\n"
"}\n"
"QPushButton{\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    padding-bottom:5px;\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_5)
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/下载.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/1jpg.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.horizontalLayout_2.addWidget(self.frame_5, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet("background-color: rgb(0, 85, 255);\n"
";\n"
"border-bottom-left-radius:30px\n"
"\n"
"    ")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_Delete = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_Delete.setStyleSheet("font: 18pt \"Algerian\";\n"
"color: rgb(255, 255, 255);\n"
"pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}\n"
"")
        self.pushButton_Delete.setObjectName("pushButton_Delete")
        self.verticalLayout_2.addWidget(self.pushButton_Delete)
        self.pushButton_Edit = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_Edit.setStyleSheet("font: 18pt \"Algerian\";\n"
"color: rgb(255, 255, 255);\n"
"pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}\n"
"\n"
"")
        self.pushButton_Edit.setObjectName("pushButton_Edit")
        self.verticalLayout_2.addWidget(self.pushButton_Edit)
        self.pushButton_New_identity = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_New_identity.setStyleSheet("font: 18pt \"Algerian\";\n"
"color: rgb(255, 255, 255);\n"
"pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}\n"
"\n"
"")
        self.pushButton_New_identity.setObjectName("pushButton_New_identity")
        self.verticalLayout_2.addWidget(self.pushButton_New_identity)
        self.horizontalLayout_4.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_8)
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_new = QtWidgets.QWidget()
        self.page_new.setObjectName("page_new")
        self.label_7 = QtWidgets.QLabel(self.page_new)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 161, 41))
        self.label_7.setStyleSheet("\n"
"font: 15pt \"Algerian\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);")
        self.label_7.setObjectName("label_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_new)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 60, 231, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_new)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 110, 231, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_identity_sure = QtWidgets.QPushButton(self.page_new)
        self.pushButton_identity_sure.setGeometry(QtCore.QRect(250, 160, 93, 28))
        self.pushButton_identity_sure.setObjectName("pushButton_identity_sure")
        self.frame_11 = QtWidgets.QFrame(self.page_new)
        self.frame_11.setGeometry(QtCore.QRect(0, 479, 641, 51))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.stackedWidget_4 = QtWidgets.QStackedWidget(self.frame_11)
        self.stackedWidget_4.setGeometry(QtCore.QRect(0, 0, 641, 51))
        self.stackedWidget_4.setObjectName("stackedWidget_4")
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.stackedWidget_4.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.label_11 = QtWidgets.QLabel(self.page_9)
        self.label_11.setGeometry(QtCore.QRect(250, 20, 161, 21))
        self.label_11.setStyleSheet("font: 12pt \"Algerian\";\n"
"color: rgb(255, 0, 0);")
        self.label_11.setObjectName("label_11")
        self.stackedWidget_4.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.label_13 = QtWidgets.QLabel(self.page_10)
        self.label_13.setGeometry(QtCore.QRect(230, 20, 161, 21))
        self.label_13.setStyleSheet("font: 12pt \"Algerian\";\n"
"color: rgb(255, 0, 0);")
        self.label_13.setObjectName("label_13")
        self.stackedWidget_4.addWidget(self.page_10)
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.label_14 = QtWidgets.QLabel(self.page_11)
        self.label_14.setGeometry(QtCore.QRect(260, 20, 111, 21))
        self.label_14.setStyleSheet("font: 12pt \"Algerian\";\n"
"color: rgb(255, 0, 0);")
        self.label_14.setObjectName("label_14")
        self.stackedWidget_4.addWidget(self.page_11)
        self.label_10 = QtWidgets.QLabel(self.page_new)
        self.label_10.setGeometry(QtCore.QRect(260, 200, 81, 16))
        self.label_10.setObjectName("label_10")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.page_new)
        self.tableWidget_3.setGeometry(QtCore.QRect(110, 220, 391, 231))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.stackedWidget.addWidget(self.page_new)
        self.page_delete = QtWidgets.QWidget()
        self.page_delete.setObjectName("page_delete")
        self.label_6 = QtWidgets.QLabel(self.page_delete)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 111, 41))
        self.label_6.setStyleSheet("\n"
"font: 15pt \"Algerian\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);")
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.page_delete)
        self.lineEdit.setGeometry(QtCore.QRect(170, 60, 261, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_close = QtWidgets.QPushButton(self.page_delete)
        self.pushButton_close.setGeometry(QtCore.QRect(250, 110, 93, 28))
        self.pushButton_close.setObjectName("pushButton_close")
        self.frame_10 = QtWidgets.QFrame(self.page_delete)
        self.frame_10.setGeometry(QtCore.QRect(0, 480, 641, 51))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.frame_10)
        self.stackedWidget_3.setGeometry(QtCore.QRect(0, 0, 641, 51))
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget_3.addWidget(self.page_3)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_4 = QtWidgets.QLabel(self.page_5)
        self.label_4.setGeometry(QtCore.QRect(260, 10, 141, 21))
        self.label_4.setStyleSheet("font: 12pt \"Algerian\";\n"
"color: rgb(255, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.stackedWidget_3.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_5 = QtWidgets.QLabel(self.page_6)
        self.label_5.setGeometry(QtCore.QRect(260, 10, 111, 21))
        self.label_5.setStyleSheet("font: 12pt \"Algerian\";\n"
"color: rgb(255, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.stackedWidget_3.addWidget(self.page_6)
        self.tableWidget = QtWidgets.QTableWidget(self.page_delete)
        self.tableWidget.setGeometry(QtCore.QRect(110, 190, 391, 231))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_3 = QtWidgets.QLabel(self.page_delete)
        self.label_3.setGeometry(QtCore.QRect(260, 170, 81, 16))
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page_delete)
        self.page_edit = QtWidgets.QWidget()
        self.page_edit.setObjectName("page_edit")
        self.label_8 = QtWidgets.QLabel(self.page_edit)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 111, 41))
        self.label_8.setStyleSheet("\n"
"font: 15pt \"Algerian\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);")
        self.label_8.setObjectName("label_8")
        self.frame_9 = QtWidgets.QFrame(self.page_edit)
        self.frame_9.setGeometry(QtCore.QRect(0, 479, 641, 40))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame_9)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(240, 10, 121, 21))
        self.label_2.setStyleSheet("font: 12pt \"Algerian\";\n"
"color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.stackedWidget_2.addWidget(self.page_2)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_12 = QtWidgets.QLabel(self.page_4)
        self.label_12.setGeometry(QtCore.QRect(210, 10, 161, 21))
        self.label_12.setStyleSheet("font: 12pt \"Algerian\";\n"
"color: rgb(255, 0, 0);")
        self.label_12.setObjectName("label_12")
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.label_25 = QtWidgets.QLabel(self.page_7)
        self.label_25.setGeometry(QtCore.QRect(240, 10, 111, 21))
        self.label_25.setStyleSheet("font: 12pt \"Algerian\";\n"
"color: rgb(255, 0, 0);")
        self.label_25.setObjectName("label_25")
        self.stackedWidget_2.addWidget(self.page_7)
        self.horizontalLayout_6.addWidget(self.stackedWidget_2)
        self.lineEdit_num = QtWidgets.QLineEdit(self.page_edit)
        self.lineEdit_num.setGeometry(QtCore.QRect(180, 110, 221, 31))
        self.lineEdit_num.setText("")
        self.lineEdit_num.setObjectName("lineEdit_num")
        self.pushButton_change_sure = QtWidgets.QPushButton(self.page_edit)
        self.pushButton_change_sure.setGeometry(QtCore.QRect(240, 180, 93, 28))
        self.pushButton_change_sure.setObjectName("pushButton_change_sure")
        self.label_9 = QtWidgets.QLabel(self.page_edit)
        self.label_9.setGeometry(QtCore.QRect(250, 220, 81, 16))
        self.label_9.setObjectName("label_9")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.page_edit)
        self.tableWidget_2.setGeometry(QtCore.QRect(100, 240, 391, 231))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.stackedWidget.addWidget(self.page_edit)
        self.horizontalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_4.addWidget(self.frame_8)
        self.verticalLayout.addWidget(self.frame_3)
        AdminWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_4.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.pushButton_2.clicked.connect(AdminWindow.close) # type: ignore
        self.pushButton.clicked.connect(AdminWindow.hide) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)

    def retranslateUi(self, AdminWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminWindow.setWindowTitle(_translate("AdminWindow", "MainWindow"))
        self.label.setText(_translate("AdminWindow", "管理员界面"))
        self.pushButton_Delete.setText(_translate("AdminWindow", "注销账户"))
        self.pushButton_Edit.setText(_translate("AdminWindow", "重置密码"))
        self.pushButton_New_identity.setText(_translate("AdminWindow", "更改用户身份"))
        self.label_7.setText(_translate("AdminWindow", "更改用户身份"))
        self.lineEdit_2.setPlaceholderText(_translate("AdminWindow", "想要更改身份的工号："))
        self.lineEdit_3.setPlaceholderText(_translate("AdminWindow", "更改后的身份等级："))
        self.pushButton_identity_sure.setText(_translate("AdminWindow", "确定"))
        self.label_11.setText(_translate("AdminWindow", "没找到该工号！"))
        self.label_13.setText(_translate("AdminWindow", "等级输入不正确！"))
        self.label_14.setText(_translate("AdminWindow", "更改成功！"))
        self.label_10.setText(_translate("AdminWindow", "用户信息表"))
        self.label_6.setText(_translate("AdminWindow", "注销账户"))
        self.lineEdit.setPlaceholderText(_translate("AdminWindow", "请输入您要注销的工号："))
        self.pushButton_close.setText(_translate("AdminWindow", "注销"))
        self.label_4.setText(_translate("AdminWindow", "没有找到工号！"))
        self.label_5.setText(_translate("AdminWindow", "注销成功！"))
        self.label_3.setText(_translate("AdminWindow", "用户信息表"))
        self.label_8.setText(_translate("AdminWindow", "重置密码"))
        self.label_2.setText(_translate("AdminWindow", "未找到工号！"))
        self.label_12.setText(_translate("AdminWindow", "两次密码不相符！"))
        self.label_25.setText(_translate("AdminWindow", "修改成功！"))
        self.lineEdit_num.setPlaceholderText(_translate("AdminWindow", "输入工号："))
        self.pushButton_change_sure.setText(_translate("AdminWindow", "确认"))
        self.label_9.setText(_translate("AdminWindow", "用户信息表"))
import res_rc
