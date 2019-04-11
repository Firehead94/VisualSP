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
from shutil import copyfile
import os


class CameraFeed(QtWidgets.QWidget):
    # Created by: Devin Yang, Leo Wernet
    # Modified by: Justin Scott

    def __init__(self):
        super(CameraFeed,self).__init__()
        self.frames_per_second = 30
        self.error_dialog = QtWidgets.QErrorMessage()

    def capture(self, fileLoc, capType, detection):
        if capType == 'GoPro':
            print("gpcam")
            self.gpCam = GoProCamera.GoPro()
            print("sock")
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.t = time()
            self.udp = "udp://10.5.5.9:8554"
            print("starting")
            try:
                self.gpCam.livestream("start")
            except:
                self.error_dialog.showMessage("No GoPro detected")
                return
            print("started")
            cap = cv.VideoCapture(self.udp)
            print("cap")
            vid = cv.VideoWriter_fourcc(*'MJPG')
        elif capType == 'File':
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;MP4 Files (*.mp4);;AVI Files (*.avi)", options=options)
            if fileName:
                if fileName[-3:] == 'avi' or fileName[-3:] == 'MP4':
                    if not (SystemUtils.getOS() == 'linux' or SystemUtils.getOS() == 'darwin'):
                        fileName = fileName.replace("/","\\")
                    print(fileName)
                    cap = cv.VideoCapture(fileName)
                    vid = cv.VideoWriter_fourcc(*'XVID')
                else:
                    self.error_dialog.showMessage("Incorrect File Type")
                    return
            else:
                print("No file selected")
                return
        elif capType == 'Webcam':
            cap = cv.VideoCapture(0)
            vid = cv.VideoWriter_fourcc(*'XVID')
        elif capType == 'None':
            self.error_dialog.showMessage("No capture device selected")
            print('No capture device selected')
            return
        else:
            self.error_dialog.showMessage("Error")
            print("error")
            return
        out = cv.VideoWriter(fileLoc, vid, self.frames_per_second, (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))))
        tracker = DetectTracker.DetectAndTrack(cap, detection)

        if cap.isOpened() != True:
            self.error_dialog.showMessage("There was an error trying to open the stream. Check if GoPro is connected to computer via WIFI")
            print("There was an error trying to open the stream. Check if GoPro is connected to computer via WIFI")
        else:
            while(True):
                #capture frames

                ret, frame = cap.read()
                if ret==True:
                    tracked = tracker.trackStuff(ret,frame, detection)
                    #display the frames
                    cv.imshow('frame', tracked) # pass tracked here to display lines, frame for dots only
                    if detection == 'ShiTomasi':
                        out.write(frame) # pass tracked here to store lines, frame for dots only
                    else:
                        out.write(tracked)

                if cv.waitKey(20) & 0xFF == ord('q'):
                    break

            #release capture
            cap.release()
            out.release()
            cv.destroyAllWindows()

