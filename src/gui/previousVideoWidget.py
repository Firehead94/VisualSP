# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/gui/previousVideoWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class previousVideoWidget(QtWidgets.QWidget):
    def __init__(self):
        super(previousVideoWidget, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.setStyleSheet("background-color: #b2b2b2;")
        self.horizontalLayoutWidget = QtWidgets.QWidget()
        self.setFixedHeight(40)

        #self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, -1, 290, 41))
        self.gridLayout_6 = QtWidgets.QGridLayout(self)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setContentsMargins(0,0,0,1)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_6.addWidget(self.horizontalLayoutWidget)
        self.name = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(18)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.name.setMargin(5)
        self.horizontalLayout.addWidget(self.name)
        self.toolButton_2 = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.toolButton_2.setStyleSheet(":hover {\n"
"    background-color: rgb(91, 103, 131);\n"
"}\n"
"QToolButton {\n"
"    border:none;\n"
"}")
        self.toolButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/assets/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout.addWidget(self.toolButton_2)
        self.toolButton = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.toolButton.setStyleSheet(":hover {\n"
"    background-color: rgb(91, 103, 131);\n"
"}\n"
"QToolButton {\n"
"    border:none;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/assets/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(30, 30))
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name.setText(_translate("Form", "Name"))
        self.toolButton.setText(_translate("Form", "..."))

import src.gui.qtresources_rc
