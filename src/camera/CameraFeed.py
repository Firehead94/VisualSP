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
        self.frames_per_second = 30

    def capture(self, fileLoc):

        cap = cv.VideoCapture('D:\\Users\\jjons\\Documents\\GitHub\\VisualSP\\GOPR5668.MP4') ###################################################
        out = cv.VideoWriter(fileLoc, cv.VideoWriter_fourcc(*'XVID'), self.frames_per_second, (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))))
        tracker = DetectTracker.DetectAndTrack(cap)

        while(True):
            #capture frames

            ret, frame = cap.read()
            if ret==True:
                tracked = tracker.trackStuff(ret,frame)
                #display the frames
                cv.imshow('frame', tracked) # pass only frame here and to out.write for dots only and no lines.
                out.write(tracked)

            if cv.waitKey(20) & 0xFF == ord('q'):
                break

        #release capture
        cap.release()
        out.release()
        cv.destroyAllWindows()

