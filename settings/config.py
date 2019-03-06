from sys import platform

DEFAULT_LOCAL_PATH_WINDOWS = "%appdata%/VisualSP2019/Users/"
DEFAULT_LOCAL_PATH_MAC = "~/Library/Preferences/visualsp/Users/"
DEFAULT_LOCAL_PATH_LINUX = "~/.visualsp/users/"
DEFAULT_LOCAL_PATH_DEFAULT = "/Users/"

DEFAULT_ACCESS_LEVEL = "0"
GENERAL_ACCESS_LEVEL = "0"
ADMIN_ACCESS_LEVEL = "10"

osType = "Default"
storage = dict(
    pathW = DEFAULT_LOCAL_PATH_WINDOWS,
    pathM = DEFAULT_LOCAL_PATH_MAC,
    pathL = DEFAULT_LOCAL_PATH_LINUX,
    pathDefault = DEFAULT_LOCAL_PATH_DEFAULT
)


def __init__(self):
    if platform == "linux":
        self.osType = "L"
    elif platform == "darwin":
        self.osType == "M"
    elif platform == "win32" or platform == "win64":
        self.osType = "W"

