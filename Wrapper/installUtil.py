import winreg
import subprocess
from subprocess import STDOUT, PIPE
import os
import sys
from pathlib import Path

studioOverride = False

def runner(argv):
	subprocess.run("attrib -r "+argv[0])
	os.rename(argv[0], argv[0]+".old") # Rename wrapper file
	os.rename(argv[0][:-4]+"_.exe", argv[0]) # Rename real file to name of wrapper file
	process = subprocess.Popen(argv, stdout=PIPE, stderr=STDOUT, universal_newlines=True) # Start the target program
	os.rename(argv[0], argv[0][:-4]+"_.exe") # Rename real file to its original name
	os.rename(argv[0]+".old", argv[0]) # Rename wrapper file to its original name
	subprocess.run("attrib +r "+argv[0])
	for stdout_line in iter(process.stdout.readline, ""): # Start reading stdout
		sys.stdout.write(stdout_line) # Output to console
		sys.stdout.flush() # Flush console
	process.stdout.close() # Close stdout

def setStudio(value=True):
	if value:
		print("Using studio settings")
	global studioOverride
	studioOverride = value

def getInstallLocation(_raw=False):
	if (not _raw) and isStudio():
		return getStudioInstallLocation()
	try:
		key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\\ROBLOX Corporation\\Environments\\roblox-player")
		pathToLauncher, type = winreg.QueryValueEx(key, None)
		path = os.path.abspath(pathToLauncher+"\\..")
		return path
	except:
		return None
def getStudioInstallLocation_2(_raw=False):
	if (not _raw) and isPlayer():
		return getInstallLocation()
	try:
		key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\\ROBLOX Corporation\\Environments\\roblox-studio")
		pathToVersions, type = winreg.QueryValueEx(key, None)
		versionId, type = winreg.QueryValueEx(key, "version")
		path = os.path.abspath(pathToVersions+"\\..\\"+versionId)
		return path
	except:
		return None
def getStudioInstallLocation(_raw=False):
	if (not _raw) and isPlayer():
		return getInstallLocation()
	try:
		key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\\ROBLOX Corporation\\Environments\\roblox-studio")
		pathToLauncher, type = winreg.QueryValueEx(key, None)
		path = os.path.abspath(pathToLauncher+"\\..")
		if Path(path).name == "Versions":
			return getStudioInstallLocation_2(_raw=_raw)
		return path
	except:
		return None

def isInVersionFolder():
	return Path(os.getcwd()).parent.name == "Versions"
def isStudio():
	return studioOverride or (os.path.isfile("RobloxStudioBeta.exe") or Path(getStudioInstallLocation(True)).name == Path(os.getcwd()).name)
def isPlayer():
	return (not isStudio()) and (os.path.isfile("RobloxPlayerBeta.exe") or Path(getInstallLocation(True)).name == Path(os.getcwd()).name)

def getInstallFiles(_includeExt=True, _allFiles=False):
	files = []
	
	if _includeExt:
		_includeExt = ".exe"
	else:
		_includeExt = ""
	
	if isPlayer() or _allFiles:
		files.append("RobloxPlayerBeta"+_includeExt)
		files.append("RobloxPlayerLauncher"+_includeExt)
	if isStudio() or _allFiles:
		files.append("RobloxStudioBeta"+_includeExt)
		files.append("RobloxStudioLauncherBeta"+_includeExt)
	return files
def getWrapperFiles(_includeExt=True, _allFiles=False):
	wfiles = []
	
	if _includeExt:
		_includeExt = ".exe"
	else:
		_includeExt = ""
	
	files = getInstallFiles(_includeExt=False, _allFiles=_allFiles)
	for fileName in files:
		wfiles.append(fileName+"_"+_includeExt)
	return wfiles

def verifyAndGoto(_installPath=None):
	if not _installPath:
		_installPath = getInstallLocation()
	if (not isInVersionFolder()):
		os.chdir(_installPath)
		return _installPath
	return False

def verifyAndMerge(_installPath=None):
	if not _installPath:
		_installPath = getInstallLocation()
	originalDir = os.getcwd()
	installPath = verifyAndGoto(_installPath)
	if installPath:
		subprocess.run("robocopy \""+originalDir+"\" \""+installPath+"\" /e", shell=True)
		return installPath
	return False