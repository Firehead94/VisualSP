import time
import datetime
import sys
import os

################################################################
#
# Contains static methods to assist with system information
# gathering.
# Created by: Justin Scott
#
################################################################

# Returns Timestamp from Epoch in mm/dd/yyyy hh:mm:ss
def getTimeStamp():
    currentTime = time.time()
    return datetime.datetime.fromtimestamp(currentTime).strftime('%m-%d-%Y %H:%M:%S')

def getOS():
    return sys.platform

