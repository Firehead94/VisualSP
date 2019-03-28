from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent

import src.datastorage.FileHelper as FileHelper
import src.datastorage.User as User
import src.gui.MainGui as MainGui
import src.utilities.SystemUtils as SystemUtils
import src.datastorage.UserHelper as UserHelper
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
import sys
import os

# Created by: Justin Scott



class MainController:


    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.gui = MainGui.MainGui()
        self.user = User.User()
        self.connectButtons()
        self.gui.VisualSP.show()

        self.videoPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoPlayer.setVideoOutput(self.gui.cameraArea)
        ## Change to local video file to display it
        #self.videoPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(FileHelper.VIDEO_FLDR + "video.avi")))
        self.videoPlayer.pause()
        ## Uncomment to play video
        #self.videoPlayer.play()

        self.gui.trackingField


        sys.exit(self.app.exec_())


    def connectButtons(self):
        #CONNECT THE BUTTONS!

        ###LOGIN BUTTONS
        self.gui.loginBtn.clicked.connect(self.loginButton)
        self.gui.newuserBtn.clicked.connect(lambda: self.gui.stackedWidget.setCurrentIndex(1))

        ###NEW USER BUTTONS
        self.gui.backBtn.clicked.connect(lambda: self.gui.stackedWidget.setCurrentIndex(0))
        self.gui.createBtn.clicked.connect(self.createButton)

        ###MAIN WINDOW BUTTONS
        self.gui.logoutBtn.clicked.connect(self.logoutButton)
        self.gui.saveBtn.clicked.connect(lambda: (self.user.save(), self.updateUserInfoPanel()))

        ##WINDOW BUTTONS
        self.gui.closeBtn.clicked.connect(self.closeBtn)
        self.gui.maxrestoreBtn.clicked.connect(self.showMaxRestore)
        self.gui.minimizeBtn.clicked.connect(self.showSmall)


    def loginButton(self):
        if os.path.isfile(FileHelper.USER_FLDR + self.gui.usernameField.text() + ".json"):
            self.user = User.loadUser(UserHelper.UserHelper.get_user(self.gui.usernameField.text()))
            self.updateUserInfoPanel()
            self.gui.stackedWidget.setCurrentIndex(2)
            return
        else:
            self.gui.ERROR_NO_EXIST.setText("<font color='red'>User Doesn't exist</font>")
        return None

    def logoutButton(self):
        self.user.save()
        UserHelper.UserHelper.update_user(self.user)
        self.updateUserInfoPanel()
        self.gui.stackedWidget.setCurrentIndex(0)

    def updateUserInfoPanel(self):
        self.gui.usernameOut.setText(self.user.user["USERNAME"])
        self.gui.firstnameOut.setText(self.user.user["FIRST_NAME"])
        self.gui.lastnameOut.setText(self.user.user["LAST_NAME"])
        self.gui.lastusedOut.setText(self.user.user["TIMESTAMP"])
        self.gui.accessLevelOut.setText(self.user.user["ACCESS_LEVEL"])

    def createButton(self):
        if os.path.isfile(FileHelper.USER_FLDR + self.gui.usernameIn.text() + ".json"):
            self.gui.ERROR_EXISTS.setText("<font color='red'>User Already Exists</font>")
        else:
            print("1")
            self.user = User.newUser(self.gui.usernameIn.text(), self.gui.firstnameIn.text(),
                                     self.gui.lastnameIn.text())
            print("2")
            if self.gui.checkBox.isChecked():
                self.user.user["ACCESS_LEVEL"] = "ADMINISTRATOR"
            else:
                self.user.user["ACCESS_LEVEL"] = "GUEST"
            print("3")
            self.user.save()
            print("4")
            self.updateUserInfoPanel()
            print("5")
            self.gui.stackedWidget.setCurrentIndex(2)

    def showSmall(self):
        self.gui.VisualSP.showMinimized()

    def showMaxRestore(self):
        if self.gui.maxNormal:
            self.gui.VisualSP.showNormal()
            self.gui.maxNormal = False
            self.gui.maxrestoreBtn.setIcon(QtGui.QIcon(":/assets/maximize.png"))
        else:
            self.gui.VisualSP.showMaximized()
            self.gui.maxNormal = True

            self.gui.maxrestoreBtn.setIcon(QtGui.QIcon(":/assets/restore.png"))

    def closeBtn(self):
        self.gui.VisualSP.close()



