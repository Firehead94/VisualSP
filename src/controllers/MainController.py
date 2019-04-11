from typing import Any, Union

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtWidgets import QWidget

import src.datastorage.FileHelper as FileHelper
import src.datastorage.User as User
import src.gui.MainGui as MainGui
import src.utilities.SystemUtils as SystemUtils
import src.datastorage.UserHelper as UserHelper
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
import sys
import os
import src.gui.previousVideoWidget as previousVideoWidget
import src.camera.CameraFeed as CameraFeed
#import src.camera.DetectTracker as DetectTracker
import src.gui.qtresources_rc

# Created by: Justin Scott
from src.camera import GproStream



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

        sys.exit(self.app.exec_())

    def populateScrollArea(self):
        #self.gui.trackingField_layout.addWidget()
        self.playing = QtWidgets.QToolButton()
        self.videoPlayer.stateChanged.connect(lambda:   self.playing.setIcon(QtGui.QIcon(":/assets/play.png")) if self.videoPlayer.state() == QMediaPlayer.StoppedState else None)
        while self.gui.trackingField_layout.count():
            item = self.gui.trackingField_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        for i in self.user.user["TRACKINGS"]:
            vidWid = previousVideoWidget.previousVideoWidget()
            vidWid.name.setText(i[len(self.user.user["USERNAME"])+1:-4])
            vidWid.toolButton.setToolTip(i)
            vidWid.toolButton.clicked.connect(self.deleteBtn)
            vidWid.toolButton_2.setToolTip(i)
            vidWid.toolButton_2.clicked.connect(self.playBtn)
            self.gui.trackingField_layout.addWidget(vidWid)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gui.trackingField_layout.addItem(spacerItem)

    def createNew(self):
        captureArea = CameraFeed.CameraFeed()
        #captureArea = GproStream.GproStream()
        time = SystemUtils.getTimeStamp().replace(" ", "_").replace(":","-")
        fileLoc = FileHelper.VIDEO_FLDR + self.user.user["USERNAME"] + "-" + time + ".avi"
        captureArea.capture(fileLoc, self.gui.Source.currentText(), self.gui.featureDetections.currentText())
        if os.path.isfile(fileLoc):
            self.user.user["TRACKINGS"].append(self.user.user["USERNAME"] + "-" + time + ".avi")
            self.gui.mediaArea.addWidget(captureArea)
            self.gui.mediaArea.setCurrentIndex(1)
            self.user.save()
            self.updateUserInfoPanel()

    ## play a
    def playBtn(self):
        self.gui.mediaArea.setCurrentIndex(0)
        if self.playing == self.gui.sender():
            if self.videoPlayer.state() == QMediaPlayer.PlayingState:
                self.gui.sender().setIcon(QtGui.QIcon(":/assets/play.png"))
                self.videoPlayer.pause()
            else:
                self.gui.sender().setIcon(QtGui.QIcon(":/assets/pause.png"))
                self.videoPlayer.play()
        else:
            fileLoc = FileHelper.VIDEO_FLDR + self.gui.sender().toolTip()
            if os.path.isfile(fileLoc):
                self.videoPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileLoc)))
                self.gui.sender().setIcon(QtGui.QIcon(":/assets/pause.png"))
                self.videoPlayer.play()
                self.playing.setIcon(QtGui.QIcon(":/assets/play.png"))
                self.playing = self.gui.sender()
            else:
                print("no file found")

    def deleteBtn(self):
        fileName = self.gui.sender().toolTip()
        fileLoc = FileHelper.VIDEO_FLDR + fileName
        self.user.user["TRACKINGS"].remove(fileName)
        if os.path.isfile(fileLoc):
            os.remove(fileLoc)
        self.user.save()
        self.updateUserInfoPanel()

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
        self.gui.menuBtn.clicked.connect(self.createNew)

        ##WINDOW BUTTONS
        self.gui.closeBtn.clicked.connect(self.closeBtn)
        self.gui.maxrestoreBtn.clicked.connect(self.showMaxRestore)
        self.gui.minimizeBtn.clicked.connect(self.showSmall)

    def loginButton(self):
        if os.path.isfile(FileHelper.USER_FLDR + self.gui.usernameField.text() + ".pkl"):
            self.user = User.loadUser(UserHelper.UserHelper.get_user(self.gui.usernameField.text()))
            self.updateUserInfoPanel()
            self.gui.featureDetections.setVisible(True)
            self.gui.Source.setVisible(True)
            self.gui.stackedWidget.setCurrentIndex(2)
            return
        else:
            self.gui.ERROR_NO_EXIST.setText("<font color='red'>User Doesn't exist</font>")
        return None

    def logoutButton(self):
        self.user.save()
        UserHelper.UserHelper.update_user(self.user)
        self.updateUserInfoPanel()
        self.gui.featureDetections.setVisible(False)
        self.gui.Source.setVisible(False)
        self.gui.stackedWidget.setCurrentIndex(0)

    def updateUserInfoPanel(self):
        self.gui.usernameOut.setText(self.user.user["USERNAME"])
        self.gui.firstnameOut.setText(self.user.user["FIRST_NAME"])
        self.gui.lastnameOut.setText(self.user.user["LAST_NAME"])
        self.gui.lastusedOut.setText(self.user.user["TIMESTAMP"])
        self.gui.accessLevelOut.setText(self.user.user["ACCESS_LEVEL"])
        self.populateScrollArea()

    def createButton(self):
        if os.path.isfile(FileHelper.USER_FLDR + self.gui.usernameIn.text() + ".pkl"):
            self.gui.ERROR_EXISTS.setText("<font color='red'>User Already Exists</font>")
        else:
            self.user = User.newUser(self.gui.usernameIn.text(), self.gui.firstnameIn.text(),
                                     self.gui.lastnameIn.text())
            if self.gui.checkBox.isChecked():
                self.user.user["ACCESS_LEVEL"] = "ADMINISTRATOR"
            else:
                self.user.user["ACCESS_LEVEL"] = "GUEST"
            self.user.save()
            self.updateUserInfoPanel()
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



