from sys import platform
import os

# Created by: Justin Scott

APPDATA_LOC = os.getenv('APPDATA')

DEFAULT_LOCAL_PATH = "\\VisualSP2019"

DEFAULT_USER_FOLDER = "\\users"
DEFAULT_VIDEO_FOLDER = "\\videos"
DEFAULT_MISC_FOLDER = "\\misc"

DEFAULT_ACCESS_LEVEL = "0"
GENERAL_ACCESS_LEVEL = "0"
ADMIN_ACCESS_LEVEL = "10"
osType = "unknown"


if platform == "linux":
    osType = "L"
elif platform == "darwin":
    osType == "M"
elif platform == "win32" or platform == "win64":
    osType = "W"

try:
    os.mkdir(APPDATA_LOC + DEFAULT_LOCAL_PATH)
except FileExistsError:
    print("Directory " , DEFAULT_LOCAL_PATH ,  " already exists")

try:
    os.mkdir(APPDATA_LOC + DEFAULT_LOCAL_PATH + DEFAULT_USER_FOLDER)
except FileExistsError:
    print("Directory " , DEFAULT_USER_FOLDER ,  " already exists")

try:
    os.mkdir(APPDATA_LOC + DEFAULT_LOCAL_PATH + DEFAULT_VIDEO_FOLDER)
except FileExistsError:
    print("Directory " , DEFAULT_VIDEO_FOLDER ,  " already exists")

try:
    os.mkdir(APPDATA_LOC + DEFAULT_LOCAL_PATH + DEFAULT_MISC_FOLDER)
except FileExistsError:
    print("Directory " , DEFAULT_MISC_FOLDER ,  " already exists")
