import os
import settings.config
import time
import datetime

################################################################
#
# Contains static methods to assist with system information
# gathering.
#
################################################################

# Returns Timestamp from Epoch in mm/dd/yyyy hh:mm:ss
def getTimeStamp():
    currentTime = time.time()
    return datetime.datetime.fromtimestamp(currentTime).strftime('%m-%d-%Y %H:%M:%S')
