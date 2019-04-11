#!/usr/bin/env python

import numpy as np
import cv2 as cv
import yaml

input = 'fast'

# Created by: Kenzie King

# Change this if using a different video source. It currently 
# uses whatever the computer has as default
#from src.datastorage import FileHelper

cap = cv.VideoCapture(0)

# Parameters for ShiTomasi corner detection (goodPointsToTrack)
feature_params = dict( maxCorners = 50,
                       qualityLevel = 0.01,
                       minDistance = 7,
                       blockSize = 3,
		       useHarrisDetector = True )

# Parameters for KLT Tracker
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

# Create random colors for use in point tracking
color = np.random.randint(0,255,(100,3))




p0 = np.zeros(shape=(1,2))
ret, old_frame = cap.read()
old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)

if (input == 'shi'):
    p0 = cv.goodFeaturesToTrack(old_gray, mask = None, **feature_params)


# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)
good_new = []
good_old = []
img = []
p1 = []


# Opens YAML file containing calibration data
fp = open( "ost.yaml", "r" )
ci = yaml.safe_load(fp)

# Extracts wanted values from YAML file
height = ci["image_height"]
width  = ci["image_width"]
distortion_model = ci["distortion_model"]
K = ci["camera_matrix"]["data"]
D = ci["distortion_coefficients"]["data"]
R = ci["rectification_matrix"]["data"]
P = ci["projection_matrix"]["data"]

# Puts camera matrix and distortion coefficients into numpy 
# arrays so they can be used for undistortion
camMat = np.array( K ).reshape((3, 3))
camDist = np.array( D ).reshape((1, 5))
camRect = np.array( R ).reshape((3, 3))

def shiRetrack():
    # Redetects points when a certain number of them dissapear
    global p1
    if (len(p1) <= 20):
        p0 = cv.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
        p1 = p0

def calc():
    global p1
    p1 = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    # Select corners
    global good_new 
    good_new = p1[st==1]
    global good_old 
    good_old = p0[st==1]


def draw(mask, undist):
    # Draw tracking data
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        mask = cv.line(mask, (a,b),(c,d), color[i].tolist(), 2)
        undist = cv.circle(frame,(a,b),5,color[i].tolist(),-1)
    global img
    img = cv.add(undist, mask)


def update(frame_gray):
    # Update the previous frame and points
    global old_gray
    old_gray = frame_gray.copy()
    global p0
    p0 = good_new.reshape(-1,1,2)

def siftSurf(old_gray, p0):
    img=cv.drawKeypoints(old_gray,kp,4, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    good_new = p1 
    good_old = p0
    old_gray = frame_gray.copy()
    p0 = np.array(good_new).reshape(-1,1,2)
    cv.imshow('frame',img)

# Main loop 
while(1):

    ret,frame = cap.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Undistorts
    undist = cv.undistort(frame, camMat, camDist, None, None) 

    if (input == 'shi'):
        shiRetrack()
        calc()
        draw(mask, undist)
        update(frame_gray)
        cv.imshow('frame',img)

    elif (input == 'sift'):
        sift = cv.xfeatures2d.SIFT_create()
        kp, des = sift.detectAndCompute(old_gray,None)
        img=cv.drawKeypoints(old_gray,kp,4, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        good_new = p1 
        good_old = p0
        old_gray = frame_gray.copy()
        p0 = np.array(good_new).reshape(-1,1,2)
        cv.imshow('frame',img)

    elif (input == 'surf'):
        surf = cv.xfeatures2d.SURF_create(1000)
        kp, des = surf.detectAndCompute(old_gray,None)
        img=cv.drawKeypoints(old_gray,kp,4, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        good_new = p1 
        good_old = p0
        old_gray = frame_gray.copy()
        p0 = np.array(good_new).reshape(-1,1,2)
        cv.imshow('frame',img)

    elif (input == 'orb'):
        orb = cv.ORB_create(nfeatures=100)
	kp, des = orb.detectAndCompute(old_gray, None)
        img=cv.drawKeypoints(old_gray,kp,4, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        good_new = p1 
        good_old = p0
        old_gray = frame_gray.copy()
        p0 = np.array(good_new).reshape(-1,1,2)
        cv.imshow('frame',img)

    elif (input == 'fast'):
        fast = cv.FastFeatureDetector_create(25, True)
    	# calls FAST algorithm using OpenCV
    	kp = fast.detect(frame, None)
    	# draws the points that FAST finds on the image
    	img = cv.drawKeypoints(old_gray, kp, None, color=(80, 0, 200))
        cv.imshow('frame',img)

    # Exit loop with specific key press (escape and x button on window)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
    if (cv.getWindowProperty('frame',cv.WND_PROP_VISIBLE) < 1):
        break

# Kill
cv.destroyAllWindows()
cap.release()
