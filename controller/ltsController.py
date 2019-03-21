from user import User, UserHelper
import json
import os
import settings.config as config
import uuid
from system import SystemHelper

# Created by: Justin Scott


# File that will handle all functions relating to analyzing the long term storage of infomation on the machine
global savePath
savePath = config.APPDATA_LOC + config.DEFAULT_LOCAL_PATH

def userExist(username):
    userLoc = savePath + config.DEFAULT_USER_FOLDER
    print(userLoc + "\\" + username + ".txt")
    return os.path.isfile(userLoc + "\\" + username + ".txt")

