import winreg
import subprocess
import os

def getInstallLocation():
	try:
		key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\\ROBLOX Corporation\\Environments\\roblox-player")
		pathToLauncher, type = winreg.QueryValueEx(key, None)
		path = os.path.abspath(pathToLauncher+"\\..")
		return path
	except:
		return None
def getStudioInstallLocation():
	try:
		key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\\ROBLOX Corporation\\Environments\\roblox-studio")
		pathToLauncher, type = winreg.QueryValueEx(key, None)
		path = os.path.abspath(pathToLauncher+"\\..")
		return path
	except:
		return None
def verifyAndGoto():
	installPath = getInstallLocation()
	if (not os.path.isfile("RobloxPlayerBeta.exe")) or (not os.path.isfile("RobloxPlayerLauncher.exe")):
		if os.path.abspath(os.getcwd()+"\\..") != os.path.abspath(installPath+"\\.."):
			os.chdir(installPath)
def verifyAndMerge():
	installPath = getInstallLocation()
	if (not os.path.isfile("RobloxPlayerBeta.exe")) or (not os.path.isfile("RobloxPlayerLauncher.exe")):
		if os.path.abspath(os.getcwd()+"\\..") != os.path.abspath(installPath+"\\.."):
			subprocess.run("robocopy \""+os.getcwd()+"\" \""+installPath+"\" /e", shell=True)
			os.chdir(installPath)