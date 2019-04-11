import os
import src.utilities.SystemUtils as SystemUtils


# Created by: Justin Scott


global ROOT_LOC
global USER_FLDR
global VIDEO_FLDR
global MISC_FLDR
global OST


if SystemUtils.getOS() == 'linux' or SystemUtils.getOS() == 'darwin':
    ROOT_LOC = os.path.expanduser('~/VisualSP2019')
    USER_FLDR = ROOT_LOC + '/users/'
    VIDEO_FLDR = ROOT_LOC + '/videos/'
    MISC_FLDR = ROOT_LOC + '/misc/'
    OST = '../camera/ost.yaml'
else:
    ROOT_LOC = os.getenv('APPDATA') + '\\VisualSP2019'
    USER_FLDR = ROOT_LOC + '\\users\\'
    VIDEO_FLDR = ROOT_LOC + '\\videos\\'
    MISC_FLDR = ROOT_LOC + '\\misc\\'
    OST = 'camera\\ost.yaml'


try:
    os.makedirs(ROOT_LOC)
except FileExistsError:
    print("Directory " , ROOT_LOC ,  " already exists")

try:
    os.makedirs(USER_FLDR)
except FileExistsError:
    print("Directory " , USER_FLDR ,  " already exists")

try:
    os.makedirs(VIDEO_FLDR)
except FileExistsError:
    print("Directory " , VIDEO_FLDR ,  " already exists")

try:
    os.makedirs(MISC_FLDR)
except FileExistsError:
    print("Directory " , MISC_FLDR ,  " already exists")
