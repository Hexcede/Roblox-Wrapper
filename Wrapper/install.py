import subprocess
import os

ahkPath = "\"Ahk2Exe\\Ahk2Exe.exe\""

import installUtil
installUtil.verifyAndMerge()

mpress = "1" # Compress ahk files (0 for don't... Probably not necessary to disable)
if (not os.path.isfile("RobloxPlayerBeta_.exe")) or (not os.path.isfile("RobloxPlayerLauncher_.exe")):
	if (not os.path.isfile("RobloxPlayerBeta.exe")) or (not os.path.isfile("RobloxPlayerLauncher.exe")):
		raise Exception("RobloxPlayerBeta.exe and RobloxPlayerLauncher.exe couldn't be located or your Roblox installation is corrupt.")
	
	subprocess.run("ren \"%cd%\\RobloxPlayerBeta.exe\" RobloxPlayerBeta_.exe", check=True, shell=True)
	subprocess.run("ren \"%cd%\\RobloxPlayerLauncher.exe\" RobloxPlayerLauncher_.exe", check=True, shell=True)
else:
	if os.path.isfile("RobloxPlayerBeta.exe"):
		subprocess.run("attrib -r RobloxPlayerBeta.exe", check=True)

if os.path.isfile("RobloxPlayerBeta_.exe") and os.path.isfile("RobloxPlayerLauncher_.exe"):
	subprocess.run(ahkPath+" /in RobloxPlayerBeta.ahk /icon Roblox.ico /mpress "+mpress)
	subprocess.run(ahkPath+" /in RobloxPlayerLauncher.ahk /icon Roblox.ico /mpress "+mpress)
	subprocess.run("attrib +r RobloxPlayerBeta.exe")