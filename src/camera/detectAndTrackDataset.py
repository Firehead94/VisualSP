#!/usr/bin/env python

import numpy as np
import cv2 as cv

# Created by: Kenzie King

# Parameters for ShiTomasi corner detection (goodPointsToTrack)
detector = cv.FastFeatureDetector_create(threshold=25, nonmaxSuppression=True)

# Parameters for KLT Tracker
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

# Take first frame and find corners in it
ret, old_frame = cap.read()
old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
p0 = cv.goodFeaturesToTrack(old_gray, mask = None, **feature_params)


good_new = []
good_old = []
img = []
p1 = []


location = '/home/xxx/datasets/KITTI_odometry_poses/00.txt'
with open(location) as f:
    self.location = f.readlines()

width = 1241.0
height = 376.0
fx = 718.8560
fy = 718.8560
cx = 607.1928
cy = 185.2157
arr = [0.0, 0.0, 0.0, 0.0, 0.0]



def calc(): #good w/ dataset
    global p1
    p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    # Select corners
    global good_new 
    good_new = p1[st==1]
    global good_old 
    good_old = p0[st==1]




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
for img_id in xrange(4541):
	img = cv2.imread('/home/dataset/sequences/00/image_0/'+str(img_id).zfill(6)+'.png', 0)


    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Undistorts
    undist = cv.undistort(frame, camMat, camDist, None, None) 

    calc()

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
