import os
import numpy as np
from PyQt5 import QtWidgets

import src.datastorage.FileHelper as FileHelper
import src.utilities.SystemUtils as SystemUtils
import src.camera.DetectTracker as DetectTracker
import cv2 as cv

# Created by: Devin Yang

class CameraFeed(QtWidgets.QWidget):

    def __init__(self):
        super(CameraFeed,self).__init__()
        self.filename = None
        self.frames_per_second = 24.0
        self.My_res = '1080p'
        #standard res
        self.STD_DIMENSIONS ={
            "480p": (640, 480),
            "720p": (1280, 720),
            "1080p": (1920, 1080)
        }

    #set res
    def change_res (self, cap, width, height):
        self.cap.set(3,width)
        self.cap.set(4,height)

    def get_dims(self, cap, res = '720p'):
        width, height = self.STD_DIMENSIONS['480p']
        if res in self.STD_DIMENSIONS:
            width, height = self.STD_DIMENSIONS[res]
        self.change_res(cap, width,height)
        return width, height

    def capture(self):
        self.cap = cv.VideoCapture(0) ###################################################
        self.dims = self.get_dims(self.cap, res=self.My_res)
        out = cv.VideoWriter(self.filename, cv.VideoWriter_fourcc(*'XVID'), self.frames_per_second, self.dims)
        tracker = DetectTracker.DetectAndTrack(self.cap)
        while(True):
            #capture frames
            ret, frame = self.cap.read()
            tracker.trackStuff(ret,frame)
            #display the frames
            cv.imshow('frame', frame)
            out.write(frame)
            if cv.waitKey(20) & 0xFF == ord('q'):
                break

        #release capture
        self.cap.release()
        out.release()
        cv.destroyAllWindows()

