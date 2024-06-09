# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Finance_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FinanceWindow(object):
    def setupUi(self, FinanceWindow):
        FinanceWindow.setObjectName("FinanceWindow")
        FinanceWindow.resize(1020, 695)
        self.centralwidget = QtWidgets.QWidget(FinanceWindow)
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
        self.label.setGeometry(QtCore.QRect(80, 10, 161, 41))
        self.label.setStyleSheet("font: 15pt \"Algerian\";\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 0, 51, 51))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}")
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/OIP-C (1).jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.pushButton_Seach = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_Seach.setStyleSheet("font: 18pt \"Algerian\";\n"
"color: rgb(255, 255, 255);\n"
"pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}\n"
"")
        self.pushButton_Seach.setObjectName("pushButton_Seach")
        self.verticalLayout_2.addWidget(self.pushButton_Seach)
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
        self.pushButton_My = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_My.setStyleSheet("font: 18pt \"Algerian\";\n"
"color: rgb(255, 255, 255);\n"
"pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}\n"
"\n"
"")
        self.pushButton_My.setObjectName("pushButton_My")
        self.verticalLayout_2.addWidget(self.pushButton_My)
        self.pushButton_Find = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_Find.setStyleSheet("font: 18pt \"Algerian\";\n"
"color: rgb(255, 255, 255);\n"
"pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}\n"
"\n"
"")
        self.pushButton_Find.setObjectName("pushButton_Find")
        self.verticalLayout_2.addWidget(self.pushButton_Find)
        self.pushButton_Change = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_Change.setStyleSheet("font: 18pt \"Algerian\";\n"
"color: rgb(255, 255, 255);\n"
"pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}\n"
"\n"
"")
        self.pushButton_Change.setObjectName("pushButton_Change")
        self.verticalLayout_2.addWidget(self.pushButton_Change)
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
        self.page_my = QtWidgets.QWidget()
        self.page_my.setObjectName("page_my")
        self.label_7 = QtWidgets.QLabel(self.page_my)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 111, 41))
        self.label_7.setStyleSheet("\n"
"font: 15pt \"Algerian\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);")
        self.label_7.setObjectName("label_7")
        self.label_13 = QtWidgets.QLabel(self.page_my)
        self.label_13.setGeometry(QtCore.QRect(100, 170, 71, 31))
        self.label_13.setStyleSheet("color: rgb(0, 85, 255);\n"
"font: 18pt \"Algerian\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.page_my)
        self.label_14.setGeometry(QtCore.QRect(250, 110, 201, 31))
        self.label_14.setStyleSheet("font: 10pt \"Arial\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.page_my)
        self.label_15.setGeometry(QtCore.QRect(100, 106, 81, 41))
        self.label_15.setStyleSheet("color: rgb(0, 85, 255);\n"
"font: 18pt \"Algerian\";")
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.page_my)
        self.label_17.setGeometry(QtCore.QRect(100, 290, 161, 31))
        self.label_17.setStyleSheet("color: rgb(0, 85, 255);\n"
"font: 18pt \"Algerian\";")
        self.label_17.setObjectName("label_17")
        self.label_19 = QtWidgets.QLabel(self.page_my)
        self.label_19.setGeometry(QtCore.QRect(100, 226, 71, 41))
        self.label_19.setStyleSheet("color: rgb(0, 85, 255);\n"
"font: 18pt \"Algerian\";")
        self.label_19.setObjectName("label_19")
        self.label_21 = QtWidgets.QLabel(self.page_my)
        self.label_21.setGeometry(QtCore.QRect(100, 420, 71, 31))
        self.label_21.setStyleSheet("color: rgb(0, 85, 255);\n"
"font: 18pt \"Algerian\";")
        self.label_21.setObjectName("label_21")
        self.label_23 = QtWidgets.QLabel(self.page_my)
        self.label_23.setGeometry(QtCore.QRect(100, 350, 91, 41))
        self.label_23.setStyleSheet("color: rgb(0, 85, 255);\n"
"font: 18pt \"Algerian\";")
        self.label_23.setObjectName("label_23")
        self.label_16 = QtWidgets.QLabel(self.page_my)
        self.label_16.setGeometry(QtCore.QRect(250, 170, 201, 31))
        self.label_16.setStyleSheet("font: 10pt \"Arial\";")
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(self.page_my)
        self.label_18.setGeometry(QtCore.QRect(250, 230, 201, 31))
        self.label_18.setStyleSheet("font: 10pt \"Arial\";")
        self.label_18.setObjectName("label_18")
        self.label_20 = QtWidgets.QLabel(self.page_my)
        self.label_20.setGeometry(QtCore.QRect(250, 290, 201, 31))
        self.label_20.setStyleSheet("font: 10pt \"Arial\";")
        self.label_20.setObjectName("label_20")
        self.label_22 = QtWidgets.QLabel(self.page_my)
        self.label_22.setGeometry(QtCore.QRect(250, 350, 201, 31))
        self.label_22.setStyleSheet("font: 10pt \"Arial\";\n"
"")
        self.label_22.setObjectName("label_22")
        self.label_24 = QtWidgets.QLabel(self.page_my)
        self.label_24.setGeometry(QtCore.QRect(250, 420, 201, 31))
        self.label_24.setStyleSheet("font: 10pt \"Arial\";\n"
"")
        self.label_24.setObjectName("label_24")
        self.stackedWidget.addWidget(self.page_my)
        self.page_salary = QtWidgets.QWidget()
        self.page_salary.setObjectName("page_salary")
        self.label_6 = QtWidgets.QLabel(self.page_salary)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 161, 41))
        self.label_6.setStyleSheet("\n"
"font: 15pt \"Algerian\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);")
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self.page_salary)
        self.label_4.setGeometry(QtCore.QRect(81, 120, 161, 41))
        self.label_4.setStyleSheet("color: rgb(0, 85, 255);\n"
"font: 18pt \"Algerian\";")
        self.label_4.setObjectName("label_4")
        self.label_10 = QtWidgets.QLabel(self.page_salary)
        self.label_10.setGeometry(QtCore.QRect(81, 184, 161, 31))
        self.label_10.setStyleSheet("color: rgb(0, 85, 255);\n"
"font: 18pt \"Algerian\";")
        self.label_10.setObjectName("label_10")
        self.label_25 = QtWidgets.QLabel(self.page_salary)
        self.label_25.setGeometry(QtCore.QRect(250, 130, 201, 31))
        self.label_25.setStyleSheet("font: 10pt \"Arial\";")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.page_salary)
        self.label_26.setGeometry(QtCore.QRect(250, 190, 201, 31))
        self.label_26.setStyleSheet("font: 10pt \"Arial\";")
        self.label_26.setObjectName("label_26")
        self.label_11 = QtWidgets.QLabel(self.page_salary)
        self.label_11.setGeometry(QtCore.QRect(81, 254, 161, 31))
        self.label_11.setStyleSheet("color: rgb(0, 85, 255);\n"
"font: 18pt \"Algerian\";")
        self.label_11.setObjectName("label_11")
        self.label_27 = QtWidgets.QLabel(self.page_salary)
        self.label_27.setGeometry(QtCore.QRect(250, 250, 201, 31))
        self.label_27.setStyleSheet("font: 10pt \"Arial\";")
        self.label_27.setObjectName("label_27")
        self.label_50 = QtWidgets.QLabel(self.page_salary)
        self.label_50.setGeometry(QtCore.QRect(250, 320, 201, 31))
        self.label_50.setStyleSheet("font: 10pt \"Arial\";")
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.page_salary)
        self.label_51.setGeometry(QtCore.QRect(80, 320, 161, 31))
        self.label_51.setStyleSheet("color: rgb(0, 85, 255);\n"
"font: 18pt \"Algerian\";")
        self.label_51.setObjectName("label_51")
        self.stackedWidget.addWidget(self.page_salary)
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
        self.horizontalLayout_6.addWidget(self.stackedWidget_2)
        self.lineEdit_change_password = QtWidgets.QLineEdit(self.page_edit)
        self.lineEdit_change_password.setGeometry(QtCore.QRect(170, 140, 221, 31))
        self.lineEdit_change_password.setText("")
        self.lineEdit_change_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_change_password.setObjectName("lineEdit_change_password")
        self.lineEdit_Rchange_password = QtWidgets.QLineEdit(self.page_edit)
        self.lineEdit_Rchange_password.setGeometry(QtCore.QRect(170, 200, 221, 31))
        self.lineEdit_Rchange_password.setText("")
        self.lineEdit_Rchange_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Rchange_password.setObjectName("lineEdit_Rchange_password")
        self.pushButton_change_sure = QtWidgets.QPushButton(self.page_edit)
        self.pushButton_change_sure.setGeometry(QtCore.QRect(230, 280, 93, 28))
        self.pushButton_change_sure.setObjectName("pushButton_change_sure")
        self.stackedWidget.addWidget(self.page_edit)
        self.page_find_other = QtWidgets.QWidget()
        self.page_find_other.setObjectName("page_find_other")
        self.tableWidget = QtWidgets.QTableWidget(self.page_find_other)
        self.tableWidget.setGeometry(QtCore.QRect(60, 60, 531, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_52 = QtWidgets.QLabel(self.page_find_other)
        self.label_52.setGeometry(QtCore.QRect(0, 0, 161, 41))
        self.label_52.setStyleSheet("\n"
"font: 15pt \"Algerian\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);")
        self.label_52.setObjectName("label_52")
        self.stackedWidget.addWidget(self.page_find_other)
        self.page_chang_eother = QtWidgets.QWidget()
        self.page_chang_eother.setObjectName("page_chang_eother")
        self.label_53 = QtWidgets.QLabel(self.page_chang_eother)
        self.label_53.setGeometry(QtCore.QRect(0, 0, 111, 41))
        self.label_53.setStyleSheet("\n"
"font: 15pt \"Algerian\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);")
        self.label_53.setObjectName("label_53")
        self.lineEdit_grade = QtWidgets.QLineEdit(self.page_chang_eother)
        self.lineEdit_grade.setGeometry(QtCore.QRect(220, 240, 201, 31))
        self.lineEdit_grade.setObjectName("lineEdit_grade")
        self.lineEdit_num = QtWidgets.QLineEdit(self.page_chang_eother)
        self.lineEdit_num.setGeometry(QtCore.QRect(220, 150, 201, 31))
        self.lineEdit_num.setObjectName("lineEdit_num")
        self.pushButton_change_money_sure = QtWidgets.QPushButton(self.page_chang_eother)
        self.pushButton_change_money_sure.setGeometry(QtCore.QRect(270, 340, 93, 28))
        self.pushButton_change_money_sure.setObjectName("pushButton_change_money_sure")
        self.frame_11 = QtWidgets.QFrame(self.page_chang_eother)
        self.frame_11.setGeometry(QtCore.QRect(0, 479, 641, 51))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.frame_11)
        self.stackedWidget_3.setGeometry(QtCore.QRect(0, 0, 641, 51))
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget_3.addWidget(self.page_3)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.label_5 = QtWidgets.QLabel(self.page_9)
        self.label_5.setGeometry(QtCore.QRect(250, 20, 101, 21))
        self.label_5.setStyleSheet("font: 12pt \"Algerian\";\n"
"color: rgb(255, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.stackedWidget_3.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.label_54 = QtWidgets.QLabel(self.page_10)
        self.label_54.setGeometry(QtCore.QRect(240, 20, 121, 31))
        self.label_54.setStyleSheet("font: 12pt \"Algerian\";\n"
"color: rgb(255, 0, 0);")
        self.label_54.setObjectName("label_54")
        self.stackedWidget_3.addWidget(self.page_10)
        self.stackedWidget.addWidget(self.page_chang_eother)
        self.horizontalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_4.addWidget(self.frame_8)
        self.verticalLayout.addWidget(self.frame_3)
        FinanceWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FinanceWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.pushButton_2.clicked.connect(FinanceWindow.close) # type: ignore
        self.pushButton.clicked.connect(FinanceWindow.hide) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(FinanceWindow)

    def retranslateUi(self, FinanceWindow):
        _translate = QtCore.QCoreApplication.translate
        FinanceWindow.setWindowTitle(_translate("FinanceWindow", "MainWindow"))
        self.label.setText(_translate("FinanceWindow", "财务管理用户"))
        self.pushButton_Seach.setText(_translate("FinanceWindow", "薪水查询"))
        self.pushButton_Edit.setText(_translate("FinanceWindow", "密码修改"))
        self.pushButton_My.setText(_translate("FinanceWindow", "我的"))
        self.pushButton_Find.setText(_translate("FinanceWindow", "查看所有\n"
"员工薪资"))
        self.pushButton_Change.setText(_translate("FinanceWindow", "修改他人薪资"))
        self.label_7.setText(_translate("FinanceWindow", "个人信息"))
        self.label_13.setText(_translate("FinanceWindow", "姓名"))
        self.label_14.setText(_translate("FinanceWindow", "TextLabel"))
        self.label_15.setText(_translate("FinanceWindow", "工号"))
        self.label_17.setText(_translate("FinanceWindow", "入职年份"))
        self.label_19.setText(_translate("FinanceWindow", "性别"))
        self.label_21.setText(_translate("FinanceWindow", "电话"))
        self.label_23.setText(_translate("FinanceWindow", "邮箱"))
        self.label_16.setText(_translate("FinanceWindow", "TextLabel"))
        self.label_18.setText(_translate("FinanceWindow", "TextLabel"))
        self.label_20.setText(_translate("FinanceWindow", "TextLabel"))
        self.label_22.setText(_translate("FinanceWindow", "TextLabel"))
        self.label_24.setText(_translate("FinanceWindow", "TextLabel"))
        self.label_6.setText(_translate("FinanceWindow", "个人薪资情况"))
        self.label_4.setText(_translate("FinanceWindow", "薪资等级"))
        self.label_10.setText(_translate("FinanceWindow", "当月工资"))
        self.label_25.setText(_translate("FinanceWindow", "TextLabel"))
        self.label_26.setText(_translate("FinanceWindow", "TextLabel"))
        self.label_11.setText(_translate("FinanceWindow", "本季度工资"))
        self.label_27.setText(_translate("FinanceWindow", "TextLabel"))
        self.label_50.setText(_translate("FinanceWindow", "TextLabel"))
        self.label_51.setText(_translate("FinanceWindow", "本年工资"))
        self.label_8.setText(_translate("FinanceWindow", "修改密码"))
        self.label_2.setText(_translate("FinanceWindow", "修改成功！"))
        self.label_12.setText(_translate("FinanceWindow", "两次密码不相符！"))
        self.lineEdit_change_password.setPlaceholderText(_translate("FinanceWindow", "输入新密码："))
        self.lineEdit_Rchange_password.setPlaceholderText(_translate("FinanceWindow", "确认密码："))
        self.pushButton_change_sure.setText(_translate("FinanceWindow", "确认"))
        self.label_52.setText(_translate("FinanceWindow", "所有员工薪资"))
        self.label_53.setText(_translate("FinanceWindow", "修改薪资"))
        self.lineEdit_grade.setPlaceholderText(_translate("FinanceWindow", "修改薪资等级："))
        self.lineEdit_num.setPlaceholderText(_translate("FinanceWindow", "输入需要修改员工的工号："))
        self.pushButton_change_money_sure.setText(_translate("FinanceWindow", "确定"))
        self.label_5.setText(_translate("FinanceWindow", "修改成功！"))
        self.label_54.setText(_translate("FinanceWindow", "工号不正确！"))
import res_rc
