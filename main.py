import win32api
import win32con
import pywintypes

devmode = pywintypes.DEVMODEType()

## set the resolution to 4/3
devmode.PelsWidth = 1024
devmode.PelsHeight = 768

devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

win32api.ChangeDisplaySettings(devmode, 0)