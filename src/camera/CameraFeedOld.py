import os
import numpy as np
from PyQt5 import QtWidgets

import src.datastorage.FileHelper as FileHelper
import src.utilities.SystemUtils as SystemUtils
import src.camera.DetectTracker as DetectTracker
import cv2 as cv

# Created by: Devin Yang

folderPath = FileHelper.VIDEO_FLDR
filename = 'video2.avi'
frames_per_second = 24.0
My_res = '1080p'

#set res
def change_res (cap, width, height):
    cap.set(3,width)
    cap.set(4,height)
#standard res
STD_DIMENSIONS ={
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
}

def get_dims(cap, res = '1080p'):
    width, height = STD_DIMENSIONS['480p']
    if res in STD_DIMENSIONS:
        width, height = STD_DIMENSIONS[res]
    change_res(cap, width,height)
    return width, height

VIDEO_TYPE = {
    'avi': cv.VideoWriter_fourcc(*'XVID'),
    'mp4': cv.VideoWriter_fourcc(*'XVID'),
}

def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE
    return VIDEO_TYPE['avi']

cap = cv.VideoCapture(0)
dims = get_dims(cap, res=My_res)
video_type_cv2 = get_video_type(filename)
print(cv.VideoWriter_fourcc(*'XVID'))
out = cv.VideoWriter(folderPath + filename, cv.VideoWriter_fourcc(*'XVID'), frames_per_second, (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))))

while(True):
    #capture frames
    ret, frame = cap.read()
    out.write(frame)
    #display the frames
    cv.imshow('frame', frame)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

#release capture
cap.release()
out.release()
cv.destroyAllWindows()