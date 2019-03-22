#TODO
import src.controllers.MainController as MainController
import sys
import src.gui.MainGui as vspGui
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
import src.datastorage.FileHelper as FileHelper
import sys
global app
from src.camera import CameraFeed as CameraFeed, detectAndTrack as OurCV



filehelper = FileHelper
#VisualSPMain.setWindowFlags(QtCore.Qt.FramelessWindowHint)
VisualSPMain = MainController.MainController()


#cam = CameraFeed
vspcv = OurCV



