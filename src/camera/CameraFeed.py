import os
import socket
from time import time

import numpy as np
from PyQt5 import QtWidgets, QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QFileDialog
from goprocam import GoProCamera

import src.datastorage.FileHelper as FileHelper
import src.utilities.SystemUtils as SystemUtils
import src.camera.DetectTracker as DetectTracker
import cv2 as cv

class CameraFeed(QtWidgets.QWidget):
    # Created by: Devin Yang

    def __init__(self):
        super(CameraFeed,self).__init__()
        self.frames_per_second = 30

    def capture(self, fileLoc, capType):

        if capType.text() == 'GoPro':
            self.gpCam = GoProCamera.GoPro()
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.t = time()
            self.udp = "udp://10.5.5.9:8554"
            self.gpCam.livestream("start")
            cap = cv.VideoCapture(self.udp)
            vid = cv.VideoWriter_fourcc(*'MJPG')
        elif capType.text() == 'File':
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;MP4 Files (*.mp4)", options=options)
            if fileName:
                cap = cv.VideoCapture(fileName)
                vid = cv.VideoWriter_fourcc(*'MP4V')
            else:
                print("No file selected")
                return
        elif capType.text() == 'Webcam':
            cap = cv.VideoCapture(0)
            vid = cv.VideoWriter_fourcc(*'XVID')
        elif capType.text() == 'None':
            print('No cap device selected')
            return
        out = cv.VideoWriter(fileLoc, vid, self.frames_per_second, (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))))
        tracker = DetectTracker.DetectAndTrack(cap)

        if cap.isOpened() != True:
            print("There was an error trying to open the stream. Check if GoPro is connected to computer via WIFI")
        else:
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

