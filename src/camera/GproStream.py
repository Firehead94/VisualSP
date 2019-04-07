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
        fps = cap.get(30)
        vid = cv.VideoWriter_fourcc(*'MJPG') # writng the video file
        out = cv.VideoWriter(fileLoc, vid, fps, (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))))
        # File = open(complete_save, "w")

        if cap.isOpened() != True:
            print("There was an error trying to open the stream.")

        while True:
            ret, frame = cap.read()
            tracked = tracker.trackStuff(ret,frame)
            ##gray = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
            cv.imshow("GoPro OpenCV", frame)
            out.write(tracked)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
            if time() - self.t >= 2.5:
                self.sock.sendto("_GPHD_:0:0:2:0.000000\n".encode(), ("10.5.5.9", 8554))
                t = time()
        # When everything is done, release the capture
        cap.release()
        out.release()
        cv.destroyAllWindows()

