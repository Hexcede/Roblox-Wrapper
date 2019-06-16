import subprocess
import os
import sys
import shutil

ahkPath = "\"Ahk2Exe\\Ahk2Exe.exe\""
from config import config, apply, save
apply(globals())

studioMode = ("--studio" in sys.argv) or ("-s" in sys.argv) # Install to studio directory
legacyMode = ("--legacy" in sys.argv) or ("-l" in sys.argv) # Enable legacy mode

config["legacyMode"] = legacyMode
save()

import installUtil
installUtil.setStudio(studioMode)

if installUtil.verifyAndMerge():
	print("Merged wrapper with latest version folder: "+installUtil.getInstallLocation())

if os.path.isdir("__pycache__"):
	shutil.rmtree("__pycache__")
	print("Updated python files")

if compressWrapper:
	compressWrapper = "1"
else:
	compressWrapper = "0"

wFiles = installUtil.getWrapperFiles()
for i, fileName in enumerate(installUtil.getInstallFiles()):
	wFileName = wFiles[i]
	if os.path.isfile(fileName[:-4]+".py"):
		if os.path.isfile(fileName):
			print("Renaming executable: "+fileName+" > "+wFileName)
			os.rename(fileName, wFileName)
		
		print("Generating wrapper executable: "+fileName+" compress="+str(compressWrapper))
		subprocess.run("attrib -r "+fileName)
		subprocess.run(ahkPath+" /in Wrapper.ahk /icon Roblox.ico /out "+fileName+" /mpress "+compressWrapper)
		subprocess.run("attrib +r "+fileName)
		if os.path.isfile(fileName):
			print("Compiled!")
		else:
			raise Exception("Failed to compile!")
	else:
		print("Skipping "+fileName+" (no python wrapper file)")
print("Install completed!")