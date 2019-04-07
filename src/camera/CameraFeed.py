import os
import numpy as np
from PyQt5 import QtWidgets, QtCore
from PyQt5 import QtGui

import src.datastorage.FileHelper as FileHelper
import src.utilities.SystemUtils as SystemUtils
import src.camera.DetectTracker as DetectTracker
import cv2 as cv

class CameraFeed(QtWidgets.QWidget):
    # Created by: Devin Yang

    def __init__(self):
        super(CameraFeed,self).__init__()
        self.frames_per_second = 24.0

    def capture(self, fileLoc):

        cap = cv.VideoCapture(0) ###################################################
        out = cv.VideoWriter(fileLoc, cv.VideoWriter_fourcc(*'XVID'), self.frames_per_second, (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))))
        tracker = DetectTracker.DetectAndTrack(cap)

        painter = QtGui.QPainter()
        while(True):
            #capture frames

            ret, frame = cap.read()

            tracked = tracker.trackStuff(ret,frame)
            #display the frames
            cv.imshow('frame', tracked) # pass only frame here and to out.write for dots only and no lines.
            out.write(tracked)
            #painter.drawImage(QtCore.QPoint(0,0), frame)
            if cv.waitKey(20) & 0xFF == ord('q'):
                break

        #release capture
        cap.release()
        out.release()
        cv.destroyAllWindows()

