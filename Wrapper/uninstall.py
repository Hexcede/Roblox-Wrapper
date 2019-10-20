import subprocess
import os
import sys
import shutil

studioMode = ("--studio" in sys.argv) or ("-s" in sys.argv) # Uninstall from studio directory
cleanup = ("--cleanup" in sys.argv) or ("-c" in sys.argv) # Cleanup files

import installUtil
installUtil.setStudio(studioMode)

if installUtil.verifyAndGoto():
	print("Found install directory")

wFiles = installUtil.getWrapperFiles(_allFiles=True)
for i, fileName in enumerate(installUtil.getInstallFiles(_allFiles=True)):
	wFileName = wFiles[i]
	if os.path.isfile(wFileName):
		if os.path.isfile(fileName):
			subprocess.run("attrib -r "+fileName)
			os.remove(fileName)
		os.rename(wFileName, fileName)
		print("Deleted compiled wrapper executable "+fileName+" and renamed real executable to original")
	else:
		print("Skipping "+fileName+" because "+wFileName+" doesn't exist")

installerPaths = ["command-window.cmd", "Icons", "Ahk2Exe", "Wrapper.ahk", "help.pyw", "install.py", "config.py", "__pycache__", "installUtil.py", "uninstall.py"]
if cleanup:
	if installUtil.isInVersionFolder():
		doCleanup = input("Are you sure you want to cleanup *all* installed files? This includes your custom python files and the Wrapper.ahk file, so be sure to back them up if they contain important code! [Y/N]")
		if doCleanup.lower() == "y":
			for path in installUtil.getInstallFiles(_includeExt=False, _allFiles=True):
				if os.path.isfile(path+".py"):
					os.remove(path+".py")
			for path in os.listdir(os.getcwd()):
				if path in installerPaths:
					if os.path.isdir(path):
						shutil.rmtree(path)
					if os.path.isfile(path):
						os.remove(path)
			print("Cleaned up files!")
			sys.exit()
		else:
			print("Did not cleanup files: Canceled")
	else:
		print("Did not clean up files: Not in a valid install directory")