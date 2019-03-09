# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIdesign.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import gui.qtresources_rc

class Ui_VisualSP(object):
    def setupUi(self, VisualSP):
        VisualSP.setObjectName("VisualSP")
        VisualSP.setEnabled(True)
        VisualSP.resize(1246, 685)
        VisualSP.setSizeIncrement(QtCore.QSize(1, 1))
        VisualSP.setAutoFillBackground(False)
        VisualSP.setStyleSheet("background-color: rgb(45, 51, 65);")
        VisualSP.setDocumentMode(False)
        VisualSP.setTabShape(QtWidgets.QTabWidget.Triangular)
        VisualSP.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks|QtWidgets.QMainWindow.GroupedDragging)
        self.Main = QtWidgets.QWidget(VisualSP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Main.sizePolicy().hasHeightForWidth())
        self.Main.setSizePolicy(sizePolicy)
        self.Main.setObjectName("Main")
        self.gridLayout = QtWidgets.QGridLayout(self.Main)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.Main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.stackedWidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.stackedWidget.setObjectName("stackedWidget")
        self.LoggedOut = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoggedOut.sizePolicy().hasHeightForWidth())
        self.LoggedOut.setSizePolicy(sizePolicy)
        self.LoggedOut.setMinimumSize(QtCore.QSize(300, 0))
        self.LoggedOut.setMaximumSize(QtCore.QSize(300, 16777215))
        self.LoggedOut.setStyleSheet("background-color: rgb(51, 58, 74);")
        self.LoggedOut.setObjectName("LoggedOut")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.LoggedOut)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.loginLabel = QtWidgets.QLabel(self.LoggedOut)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginLabel.sizePolicy().hasHeightForWidth())
        self.loginLabel.setSizePolicy(sizePolicy)
        self.loginLabel.setMinimumSize(QtCore.QSize(80, 0))
        self.loginLabel.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(48)
        self.loginLabel.setFont(font)
        self.loginLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loginLabel.setObjectName("loginLabel")
        self.verticalLayout.addWidget(self.loginLabel)
        self.login = QtWidgets.QWidget(self.LoggedOut)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login.sizePolicy().hasHeightForWidth())
        self.login.setSizePolicy(sizePolicy)
        self.login.setMinimumSize(QtCore.QSize(0, 60))
        self.login.setMaximumSize(QtCore.QSize(16777215, 60))
        self.login.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.login.setObjectName("login")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.login)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(14, 7, 265, 63))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.usernameField = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(26)
        self.usernameField.setFont(font)
        self.usernameField.setStyleSheet("background-color: rgb(111, 127, 161);")
        self.usernameField.setFrame(False)
        self.usernameField.setObjectName("usernameField")
        self.horizontalLayout_4.addWidget(self.usernameField)
        self.loginBtn = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.loginBtn.setStyleSheet(":hover {\n"
"    background-color: rgb(91, 103, 131);\n"
"}\n"
"\n"
"QToolButton {\n"
"\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/assets/arrowRight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginBtn.setIcon(icon)
        self.loginBtn.setIconSize(QtCore.QSize(25, 35))
        self.loginBtn.setObjectName("loginBtn")
        self.horizontalLayout_4.addWidget(self.loginBtn)
        self.verticalLayout.addWidget(self.login)
        self.ERROR_NO_EXIST = QtWidgets.QLabel(self.LoggedOut)
        self.ERROR_NO_EXIST.setText("")
        self.ERROR_NO_EXIST.setObjectName("ERROR_NO_EXIST")
        self.verticalLayout.addWidget(self.ERROR_NO_EXIST)
        self.newuserBtn = QtWidgets.QToolButton(self.LoggedOut)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newuserBtn.sizePolicy().hasHeightForWidth())
        self.newuserBtn.setSizePolicy(sizePolicy)
        self.newuserBtn.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(26)
        self.newuserBtn.setFont(font)
        self.newuserBtn.setStyleSheet("QToolButton {\n"
"    background-color: rgb(75, 85, 109);\n"
"}\n"
"\n"
":hover {\n"
"    background-color: rgb(91, 103, 131);\n"
"}\n"
"")
        self.newuserBtn.setObjectName("newuserBtn")
        self.verticalLayout.addWidget(self.newuserBtn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.LoggedOut)
        self.NewUser = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewUser.sizePolicy().hasHeightForWidth())
        self.NewUser.setSizePolicy(sizePolicy)
        self.NewUser.setMinimumSize(QtCore.QSize(300, 0))
        self.NewUser.setMaximumSize(QtCore.QSize(300, 16777215))
        self.NewUser.setObjectName("NewUser")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.NewUser)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.containerWidgetNew = QtWidgets.QWidget(self.NewUser)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.containerWidgetNew.sizePolicy().hasHeightForWidth())
        self.containerWidgetNew.setSizePolicy(sizePolicy)
        self.containerWidgetNew.setMinimumSize(QtCore.QSize(0, 200))
        self.containerWidgetNew.setObjectName("containerWidgetNew")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.containerWidgetNew)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ERROR_EXISTS = QtWidgets.QLabel(self.containerWidgetNew)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(20)
        self.ERROR_EXISTS.setFont(font)
        self.ERROR_EXISTS.setStyleSheet("color: rgb(255, 0, 0);")
        self.ERROR_EXISTS.setText("")
        self.ERROR_EXISTS.setObjectName("ERROR_EXISTS")
        self.verticalLayout_5.addWidget(self.ERROR_EXISTS)
        self.usernameIn = QtWidgets.QLineEdit(self.containerWidgetNew)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(20)
        self.usernameIn.setFont(font)
        self.usernameIn.setStyleSheet("background-color: rgb(111, 127, 161);")
        self.usernameIn.setObjectName("usernameIn")
        self.verticalLayout_5.addWidget(self.usernameIn)
        self.firstnameIn = QtWidgets.QLineEdit(self.containerWidgetNew)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(20)
        self.firstnameIn.setFont(font)
        self.firstnameIn.setStyleSheet("background-color: rgb(111, 127, 161);")
        self.firstnameIn.setFrame(False)
        self.firstnameIn.setObjectName("firstnameIn")
        self.verticalLayout_5.addWidget(self.firstnameIn)
        self.lastnameIn = QtWidgets.QLineEdit(self.containerWidgetNew)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(20)
        self.lastnameIn.setFont(font)
        self.lastnameIn.setStyleSheet("background-color: rgb(111, 127, 161);")
        self.lastnameIn.setFrame(False)
        self.lastnameIn.setObjectName("lastnameIn")
        self.verticalLayout_5.addWidget(self.lastnameIn)
        self.checkBox = QtWidgets.QCheckBox(self.containerWidgetNew)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(20)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("QCheckBox::indicator:unchecked:hover {\n"
"    background-color: rgb(91, 103, 131);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: rgb(91, 103, 131);\n"
"}\n"
"QCheckBox::indicator {\n"
"    image: url(:/assets/arrowRight.png);\n"
"    width: 50px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"\n"
"background-color: rgb(111, 127, 161);")
        self.checkBox.setIconSize(QtCore.QSize(15, 15))
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_5.addWidget(self.checkBox)
        self.createBtn = QtWidgets.QPushButton(self.containerWidgetNew)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(26)
        self.createBtn.setFont(font)
        self.createBtn.setStyleSheet("QToolButton {\n"
"    background-color: rgb(75, 85, 109);\n"
"}\n"
"\n"
":hover {\n"
"    background-color: rgb(91, 103, 131);\n"
"}\n"
"")
        self.createBtn.setObjectName("createBtn")
        self.verticalLayout_5.addWidget(self.createBtn)
        self.backBtn = QtWidgets.QPushButton(self.containerWidgetNew)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(26)
        self.backBtn.setFont(font)
        self.backBtn.setStyleSheet("QToolButton {\n"
"    background-color: rgb(75, 85, 109);\n"
"}\n"
"\n"
":hover {\n"
"    background-color: rgb(91, 103, 131);\n"
"}\n"
"")
        self.backBtn.setObjectName("backBtn")
        self.verticalLayout_5.addWidget(self.backBtn)
        self.verticalLayout_3.addWidget(self.containerWidgetNew)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.NewUser)
        self.LoggedIn = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoggedIn.sizePolicy().hasHeightForWidth())
        self.LoggedIn.setSizePolicy(sizePolicy)
        self.LoggedIn.setMinimumSize(QtCore.QSize(300, 0))
        self.LoggedIn.setMaximumSize(QtCore.QSize(300, 1165))
        self.LoggedIn.setStyleSheet("background-color: rgb(51, 58, 74);")
        self.LoggedIn.setObjectName("LoggedIn")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.LoggedIn)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.menuBar = QtWidgets.QWidget(self.LoggedIn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuBar.sizePolicy().hasHeightForWidth())
        self.menuBar.setSizePolicy(sizePolicy)
        self.menuBar.setMinimumSize(QtCore.QSize(225, 55))
        self.menuBar.setMaximumSize(QtCore.QSize(300, 55))
        self.menuBar.setStyleSheet("background-color: rgb(75, 85, 109);")
        self.menuBar.setObjectName("menuBar")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.menuBar)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(-1, -7, 300, 73))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.menuBtn = QtWidgets.QToolButton(self.horizontalLayoutWidget_4)
        self.menuBtn.setStyleSheet(":hover {\n"
"    background-color: rgb(91, 103, 131);\n"
"}\n"
"\n"
"QToolButton {\n"
"    border:none;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/assets/menuBars.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuBtn.setIcon(icon1)
        self.menuBtn.setIconSize(QtCore.QSize(60, 50))
        self.menuBtn.setObjectName("menuBtn")
        self.horizontalLayout_2.addWidget(self.menuBtn)
        self.saveBtn = QtWidgets.QToolButton(self.horizontalLayoutWidget_4)
        self.saveBtn.setStyleSheet(":hover {\n"
"    background-color: rgb(91, 103, 131);\n"
"}\n"
"\n"
"QToolButton {\n"
"    border:none;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Git/assets/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBtn.setIcon(icon2)
        self.saveBtn.setIconSize(QtCore.QSize(60, 50))
        self.saveBtn.setObjectName("saveBtn")
        self.horizontalLayout_2.addWidget(self.saveBtn)
        self.logoutBtn = QtWidgets.QToolButton(self.horizontalLayoutWidget_4)
        self.logoutBtn.setStyleSheet(":hover {\n"
"    background-color: rgb(91, 103, 131);\n"
"}\n"
"\n"
"QToolButton {\n"
"    border:none;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Git/assets/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logoutBtn.setIcon(icon3)
        self.logoutBtn.setIconSize(QtCore.QSize(60, 50))
        self.logoutBtn.setObjectName("logoutBtn")
        self.horizontalLayout_2.addWidget(self.logoutBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.menuBar)
        self.info = QtWidgets.QWidget(self.LoggedIn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info.sizePolicy().hasHeightForWidth())
        self.info.setSizePolicy(sizePolicy)
        self.info.setMinimumSize(QtCore.QSize(225, 240))
        self.info.setMaximumSize(QtCore.QSize(300, 240))
        self.info.setObjectName("info")
        self.verticalWidget_4 = QtWidgets.QWidget(self.info)
        self.verticalWidget_4.setGeometry(QtCore.QRect(9, 3, 279, 233))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_4.sizePolicy().hasHeightForWidth())
        self.verticalWidget_4.setSizePolicy(sizePolicy)
        self.verticalWidget_4.setMinimumSize(QtCore.QSize(0, 200))
        self.verticalWidget_4.setObjectName("verticalWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.usernameOut = QtWidgets.QLabel(self.verticalWidget_4)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.usernameOut.setFont(font)
        self.usernameOut.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.usernameOut.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.usernameOut.setObjectName("usernameOut")
        self.verticalLayout_4.addWidget(self.usernameOut)
        self.firstnameOut = QtWidgets.QLineEdit(self.verticalWidget_4)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(20)
        self.firstnameOut.setFont(font)
        self.firstnameOut.setStyleSheet("background-color: rgb(111, 127, 161);")
        self.firstnameOut.setFrame(False)
        self.firstnameOut.setObjectName("firstnameOut")
        self.verticalLayout_4.addWidget(self.firstnameOut)
        self.lastnameOut = QtWidgets.QLineEdit(self.verticalWidget_4)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(20)
        self.lastnameOut.setFont(font)
        self.lastnameOut.setStyleSheet("background-color: rgb(111, 127, 161);")
        self.lastnameOut.setFrame(False)
        self.lastnameOut.setObjectName("lastnameOut")
        self.verticalLayout_4.addWidget(self.lastnameOut)
        self.lastusedOut = QtWidgets.QLineEdit(self.verticalWidget_4)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(20)
        self.lastusedOut.setFont(font)
        self.lastusedOut.setStyleSheet("background-color: rgb(111, 127, 161);")
        self.lastusedOut.setFrame(False)
        self.lastusedOut.setObjectName("lastusedOut")
        self.verticalLayout_4.addWidget(self.lastusedOut)
        self.accessLevelOut = QtWidgets.QLineEdit(self.verticalWidget_4)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(20)
        self.accessLevelOut.setFont(font)
        self.accessLevelOut.setStyleSheet("background-color: rgb(111, 127, 161);")
        self.accessLevelOut.setFrame(False)
        self.accessLevelOut.setReadOnly(True)
        self.accessLevelOut.setObjectName("accessLevelOut")
        self.verticalLayout_4.addWidget(self.accessLevelOut)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.setStretch(3, 1)
        self.verticalLayout_4.setStretch(4, 1)
        self.verticalLayout_2.addWidget(self.info)
        self.scrollLabel = QtWidgets.QWidget(self.LoggedIn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollLabel.sizePolicy().hasHeightForWidth())
        self.scrollLabel.setSizePolicy(sizePolicy)
        self.scrollLabel.setMinimumSize(QtCore.QSize(0, 50))
        self.scrollLabel.setObjectName("scrollLabel")
        self.trackingLabel = QtWidgets.QLabel(self.scrollLabel)
        self.trackingLabel.setGeometry(QtCore.QRect(8, 2, 273, 43))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trackingLabel.sizePolicy().hasHeightForWidth())
        self.trackingLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.trackingLabel.setFont(font)
        self.trackingLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.trackingLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.trackingLabel.setObjectName("trackingLabel")
        self.verticalLayout_2.addWidget(self.scrollLabel)
        self.trackings = QtWidgets.QWidget(self.LoggedIn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trackings.sizePolicy().hasHeightForWidth())
        self.trackings.setSizePolicy(sizePolicy)
        self.trackings.setMinimumSize(QtCore.QSize(0, 300))
        self.trackings.setSizeIncrement(QtCore.QSize(0, 1))
        self.trackings.setObjectName("trackings")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.trackings)
        self.scrollArea_2.setGeometry(QtCore.QRect(-1, -2, 282, 803))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setLineWidth(0)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.trackingField = QtWidgets.QWidget()
        self.trackingField.setGeometry(QtCore.QRect(0, 0, 280, 801))
        self.trackingField.setObjectName("trackingField")
        self.scrollArea_2.setWidget(self.trackingField)
        self.verticalLayout_2.addWidget(self.trackings)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 3)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 6)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.LoggedIn)
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        self.cameraArea = QtWidgets.QFrame(self.Main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cameraArea.sizePolicy().hasHeightForWidth())
        self.cameraArea.setSizePolicy(sizePolicy)
        self.cameraArea.setStyleSheet("background-color: rgb(45, 51, 65);\n"
"background-image:    url(:/assets/camera.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.cameraArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cameraArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cameraArea.setObjectName("cameraArea")
        self.horizontalLayout_3.addWidget(self.cameraArea)
        self.horizontalLayout_3.setStretch(1, 4)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        VisualSP.setCentralWidget(self.Main)

        self.retranslateUi(VisualSP)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(VisualSP)

    def retranslateUi(self, VisualSP):
        _translate = QtCore.QCoreApplication.translate
        VisualSP.setWindowTitle(_translate("VisualSP", "MainWindow"))
        self.loginLabel.setText(_translate("VisualSP", "Login"))
        self.usernameField.setPlaceholderText(_translate("VisualSP", "Username"))
        self.loginBtn.setText(_translate("VisualSP", "..."))
        self.loginBtn.setShortcut(_translate("VisualSP", "Return"))
        self.newuserBtn.setText(_translate("VisualSP", "New User"))
        self.usernameIn.setPlaceholderText(_translate("VisualSP", "Username"))
        self.firstnameIn.setPlaceholderText(_translate("VisualSP", "First Name"))
        self.lastnameIn.setPlaceholderText(_translate("VisualSP", "Last Name"))
        self.checkBox.setText(_translate("VisualSP", "Administrator"))
        self.createBtn.setText(_translate("VisualSP", "Create"))
        self.backBtn.setText(_translate("VisualSP", "Back"))
        self.menuBtn.setText(_translate("VisualSP", "..."))
        self.saveBtn.setText(_translate("VisualSP", "..."))
        self.logoutBtn.setText(_translate("VisualSP", "..."))
        self.usernameOut.setText(_translate("VisualSP", "USERNAME"))
        self.firstnameOut.setPlaceholderText(_translate("VisualSP", "First Name"))
        self.lastnameOut.setPlaceholderText(_translate("VisualSP", "Last Name"))
        self.lastusedOut.setPlaceholderText(_translate("VisualSP", "Last Used"))
        self.accessLevelOut.setPlaceholderText(_translate("VisualSP", "Access Level"))
        self.trackingLabel.setText(_translate("VisualSP", "Previous Trackings"))



#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    VisualSP = QtWidgets.QMainWindow()
#    ui = Ui_VisualSP()
#    ui.setupUi(VisualSP)
#    VisualSP.show()
#    sys.exit(app.exec_())
