import gui.vspGui as vspGui
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
import user.User
import user.UserHelper
import settings.config
import sys
import keyboard
global app
global VisualSPMain
global ui


# Created by: Justin Scott

class loginController:

    sceneSwitcher = None


    def __init__(self):
        global VisualSPMain
        global app
        global ui
        app = QtWidgets.QApplication(sys.argv)
        VisualSPMain = QtWidgets.QMainWindow()
        ui = vspGui.Ui_VisualSP()
        ui.setupUi(VisualSPMain)
        #VisualSPMain.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        VisualSPMain.show()
        sys.exit(app.exec_())


    def switchScenes(self, sceneName):
        None

    def login(self, username):
        #Verify Login
        #Get User object
        self.switchScenes("loggedin")

    def newUser(self):
        self.switchScenes("newuser")



loginController()


