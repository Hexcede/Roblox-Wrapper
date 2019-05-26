import subprocess
import os

import installUtil
installUtil.verifyAndGoto()

#subprocess.run("python uninstall.py", check=True)
import uninstall

files = [
	"help.pyw",
	"install.py",
	"uninstall.py",
	"RobloxPlayerLauncher.ahk",
	"RobloxPlayerBeta.ahk",
	"Roblox.ico",
	"installUtil.py"
]

directories = [
	"__pycache__",
	"Ahk2Exe"
]

for file in files:
	try:
		subprocess.run("del \""+file+"\"", shell=True, stdout=None, stderr=None)
	except:
		None
for directory in directories:
	try:
		subprocess.run("rmdir /q /s \""+directory+"\"", shell=True, stdout=None, stderr=None)
	except:
		None
print("Finished cleanup. Press any key to exit.")
os.system("pause>nul")