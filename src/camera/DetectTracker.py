#!/usr/bin/env python

import numpy as np
import cv2 as cv
import yaml

# Created by: Kenzie King
# Modified by: Justin Scott
from src.datastorage import FileHelper


class DetectAndTrack():

    def __init__(self, capture):
        self.count = 0
        # Change this if using a different video source. It currently
        # uses whatever the computer has as default
        self.cap = capture

        # Parameters for ShiTomasi corner detection (goodPointsToTrack)
        self.feature_params = dict( maxCorners = 50,
                                    qualityLevel = 0.01,
                                    minDistance = 7,
                                    blockSize = 3,
                                    useHarrisDetector = True )

        # Parameters for KLT Tracker
        self.lk_params = dict( winSize  = (15,15),
                               maxLevel = 2,
                               criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

        # Create random colors for use in point tracking
        self.color = np.random.randint(0,255,(100,3))

        # Take first frame and find corners in it
        self.ret, self.old_frame = self.cap.read()
        self.old_gray = cv.cvtColor(self.old_frame, cv.COLOR_BGR2GRAY)
        self.p0 = cv.goodFeaturesToTrack(self.old_gray, mask = None, **self.feature_params)

        # Create a mask image for drawing purposes
        self.mask = np.zeros_like(self.old_frame)
        self.good_new = []
        self.good_old = []
        self.img = []
        self.p1 = []
        # Opens YAML file containing calibration data
        self.fp = open( FileHelper.OST, "r" )
        self.ci = yaml.safe_load(self.fp)

        # Extracts wanted values from YAML file
        self.height = self.ci["image_height"]
        self.width  = self.ci["image_width"]
        self.distortion_model = self.ci["distortion_model"]
        self.K = self.ci["camera_matrix"]["data"]
        self.D = self.ci["distortion_coefficients"]["data"]
        self.R = self.ci["rectification_matrix"]["data"]
        self.P = self.ci["projection_matrix"]["data"]

        # Puts camera matrix and distortion coefficients into numpy
        # arrays so they can be used for undistortion
        self.camMat = np.array( self.K ).reshape((3, 3))
        self.camDist = np.array( self.D ).reshape((1, 5))
        #NEW#
        self.camRect = np.array( self.R ).reshape((3, 3))
        global new_R
        new_R = np.zeros((256, 256), dtype = "float")
        global t
        t = np.zeros((256, 256), dtype = "float")

        traj = np.zeros((600,600,3), dtype=np.uint8)

    def calc(self):
        self.p1, self.st, self.err = cv.calcOpticalFlowPyrLK(self.old_gray, self.frame_gray, self.p0, None, **self.lk_params)
        # Select corners
        self.good_new = self.p1[self.st==1]
        self.good_old = self.p0[self.st==1]

    def draw(self, mask, undist):
        # Draw tracking data
        for i,(new,old) in enumerate(zip(self.good_new,self.good_old)):
            a,b = new.ravel()
            c,d = old.ravel()
            mask = cv.line(mask, (a,b),(c,d), self.color[i].tolist(), 2)
            undist = cv.circle(self.frame,(a,b),5,self.color[i].tolist(),-1)
        self.img = cv.add(undist, mask)


    def update(self,frame_gray):
        # Update the previous frame and points
        self.old_gray = frame_gray.copy()
        self.p0 = self.good_new.reshape(-1,1,2)


    #NEW#
    def essentialMat(self):
        self.E = cv.findEssentialMat(self.p1, self.p0, 1.0, (0,0), cv.RANSAC, .999, 1)

    # Main loop
    #while(1):
    def trackStuff(self, ret, frame):
        global new_R
        global t


        self.frame = frame
        self.ret = ret

        self.frame_gray = cv.cvtColor(self.frame, cv.COLOR_BGR2GRAY)

        # Undistorts
        undist = cv.undistort(self.frame, self.camMat, self.camDist, None, None)

        self.calc()

        self.draw(self.mask, undist)

        self.update(self.frame_gray)

        # Redetects points when a certain number of them dissapear
        if (len(self.p1) <= 20):
            self.p0 = cv.goodFeaturesToTrack(self.old_gray, mask = None, **self.feature_params)
            #NEW#
            self.p1 = self.p0

        #NEW#
        if (len(self.p1) > len(self.p0)):
            length = len(self.p1) - len(self.p0)
            self.p1 = self.p1[:-length]
        if (self.count > 0):
            #essentialMat()
            self.E, new_mask = cv.findEssentialMat(self.p1, self.p0, 1.0, (0,0), cv.RANSAC, .999, 1)
            #cv.decomposeEssentialMat(E, R0, R1, t)
            cv.recoverPose(self.E, self.p1, self.p0, new_R, t, 1.0, (0.0, 0.0), new_mask)

        self.count += 1

        #essentialMat() -- in progress

        return self.img
        # Show window
        #cv.imshow('undistorted image with trackers',self.img)

        # Exit loop with specific key press (escape and x button on window)
        #k = cv.waitKey(30) & 0xff
        #if k == 27:
        #    break
        #if cv.getWindowProperty('undistorted image with trackers',cv.WND_PROP_VISIBLE) < 1:
        #    break

    # Kill
    #cv.destroyAllWindows()
    #d.cap.release()
