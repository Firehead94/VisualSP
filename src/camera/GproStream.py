import cv2
import numpy as np
from os.path import join
from time import time
import socket
import src.datastorage.FileHelper as FileHelper
import src.camera.DetectTracker as DetectTracker
from goprocam import GoProCamera
from goprocam import constants

folderPath = FileHelper.VIDEO_FLDR
gpCam = GoProCamera.GoPro()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
t = time()
udp = "udp://10.5.5.9:8554"
File_Output = 'output.avi'
gpCam.livestream("start")
# save_path = '/‎Users/leowernet/Documents/'
# complete_save = join(save_path, File_Output)
cap = cv2.VideoCapture(udp)
tracker = DetectTracker.DetectAndTrack(cap)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = cap.get(5)
vid = cv2.VideoWriter_fourcc(*'MJPG') # writng the video file
out = cv2.VideoWriter(folderPath + File_Output, vid, fps, (frame_width, frame_height))
# File = open(complete_save, "w")

if cap.isOpened() != True:
    print("There was an error trying to open the stream.")

while True:
    ret, frame = cap.read()
    tracked = tracker.trackStuff(ret,frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    cv2.imshow("GoPro OpenCV", tracked)
    out.write(tracked)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if time() - t >= 2.5:
        sock.sendto("_GPHD_:0:0:2:0.000000\n".encode(), ("10.5.5.9", 8554))
        t = time()
# When everything is done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()