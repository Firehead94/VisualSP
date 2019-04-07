#!/usr/bin/env python

import numpy as np
import cv2 as cv
import yaml

# Created by: Kenzie King

# Change this if using a different video source. It currently 
# uses whatever the computer has as default
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

# Take first frame and find corners in it
ret, old_frame = cap.read()
old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
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

global new_R
new_R = np.zeros((256, 256), dtype = "float")
global t
t = np.zeros((256, 256), dtype = "float")

traj = np.zeros((600,600,3), dtype=np.uint8)


def calc():
    global p1
    p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
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


# In progress
def essentialMat():

    E = cv.findEssentialMat(p1, p0, 1.0, (0,0), cv.RANSAC, .999, 1)


count = 0
# Main loop 
while(1):

    ret,frame = cap.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Undistorts
    undist = cv.undistort(frame, camMat, camDist, None, None) 

    calc()

    draw(mask, undist)

    update(frame_gray)

    # Redetects points when a certain number of them dissapear
    if (len(p1) <= 20):
        p0 = cv.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
        p1 = p0
    print(len(p0))
    print("!!!!!!!!!!!!!!!!!!!!!!")
    print(len(p1))
    print("***********************")

    #print (p0)
    if (len(p1) > len(p0)):
        length = len(p1) - len(p0)
        p1 = p1[:-length]        
    if (count > 0):
    #essentialMat()
        E, new_mask = cv.findEssentialMat(p1, p0, 1.0, (0,0), cv.RANSAC, .999, 1)
	#cv.decomposeEssentialMat(E, R0, R1, t)
        print(E) 
        cv.recoverPose(E, p1, p0, new_R, t, 1.0, (0.0, 0.0), new_mask)
        print(new_R)

    count += 1

    # Show window
    cv.imshow('undistorted image with trackers',img)

    # Exit loop with specific key press (escape and x button on window)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
    if cv.getWindowProperty('undistorted image with trackers',cv.WND_PROP_VISIBLE) < 1:
        break

# Kill
cv.destroyAllWindows()
cap.release()
