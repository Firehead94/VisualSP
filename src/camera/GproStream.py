import cv2 as cv
import numpy as np
from os.path import join
from time import time
import socket

from PyQt5 import QtWidgets

import src.datastorage.FileHelper as FileHelper
import src.camera.DetectTracker as DetectTracker
from goprocam import GoProCamera
from goprocam import constants

# Created by: Leo Wernet, Devin Yang

class GproStream(QtWidgets.QWidget):

    def __init__(self):
        super(GproStream,self).__init__()
        self.folderPath = FileHelper.VIDEO_FLDR
        self.gpCam = GoProCamera.GoPro()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.t = time()
        self.udp = "udp://10.5.5.9:8554"
        self.File_Output = 'output.avi'
        self.gpCam.livestream("start")


    def capture(self, fileLoc):

        cap = cv.VideoCapture(self.udp)
        tracker = DetectTracker.DetectAndTrack(cap)
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        fps = 24
        vid = cv.VideoWriter_fourcc(*'MJPG') # writng the video file
        out = cv.VideoWriter(fileLoc, vid, fps, (frame_width, frame_height))

        if cap.isOpened() != True:
            print("There was an error trying to open the stream. Check if GoPro is connected to computer via WIFI")

        else:

            while True:
                ret, frame = cap.read()
                if ret==True:
                    tracked = tracker.trackStuff(ret, frame)
                    ##gray = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
                    cv.imshow("GoPro OpenCV", tracked)
                    out.write(tracked)

                if time() - self.t >= 2.5:
                    self.sock.sendto("_GPHD_:0:0:2:0.000000\n".encode(), ("10.5.5.9", 8554))
                    t = time()
                if cv.waitKey(1) & 0xFF == ord('q'):
                    break

        # When everything is done, release the capture
        cap.release()
        out.release()
        cv.destroyAllWindows()


