import os
import src.utilities.SystemUtils as SystemUtils

global ROOT_LOC
global USER_FLDR
global VIDEO_FLDR
global MISC_FLDR


if SystemUtils.getOS() == 'linux' or SystemUtils.getOS() == 'darwin':
    ROOT_LOC = '~/VisualSP2019'
    USER_FLDR = ROOT_LOC + '/users/'
    VIDEO_FLDR = ROOT_LOC + '/videos/'
    MISC_FLDR = ROOT_LOC + '/misc/'
else:
    ROOT_LOC = os.getenv('APPDATA') + '\\VisualSP2019'
    USER_FLDR = ROOT_LOC + '\\users\\'
    VIDEO_FLDR = ROOT_LOC + '\\videos\\'
    MISC_FLDR = ROOT_LOC + '\\misc\\'


try:
    os.mkdir(ROOT_LOC)
except FileExistsError:
    print("Directory " , ROOT_LOC ,  " already exists")

try:
    os.mkdir(USER_FLDR)
except FileExistsError:
    print("Directory " , USER_FLDR ,  " already exists")

try:
    os.mkdir(VIDEO_FLDR)
except FileExistsError:
    print("Directory " , VIDEO_FLDR ,  " already exists")

try:
    os.mkdir(MISC_FLDR)
except FileExistsError:
    print("Directory " , MISC_FLDR ,  " already exists")
