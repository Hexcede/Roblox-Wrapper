import subprocess
import os

subprocess.run("python uninstall.py", check=True)

files = [
	"help.pyw",
	"install.py",
	"uninstall.py",
	"RobloxPlayerLauncher.ahk",
	"RobloxPlayerBeta.ahk",
	"Roblox.ico",
	"Ahk2Exe\\"
]

for file in files:
	subprocess.run("del \""+file+"\"", shell=True, stdout=None, stderr=None)
print("Finished cleanup. Press any key to exit")
os.system("pause>nul")