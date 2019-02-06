from sys import platform

DEFAULT_LOCAL_PATH_WINDOWS = "%appdata%/VisualSP2019/Users/"
DEFAULT_LOCAL_PATH_MAC = "~/Library/Preferences"
DEFAULT_LOCAL_PATH_LINUX =  "~/.visualsp"


osType = "W"
if platform == "linux":
    osType = "L"
elif platform == "darwin":
    osType == "M"
elif platform == "win32" or platform == "win64":
    osType = "W"

storage = dict(
    pathW = DEFAULT_LOCAL_PATH_WINDOWS,
    pathM = DEFAULT_LOCAL_PATH_MAC,
    pathL = DEFAULT_LOCAL_PATH_LINUX,
)



