import subprocess
import os

import installUtil
installUtil.verifyAndGoto()

if os.path.isfile("RobloxPlayerBeta_.exe") and os.path.isfile("RobloxPlayerLauncher_.exe"):
	if os.path.isfile("RobloxPlayerBeta.exe"):
		subprocess.run("attrib -r RobloxPlayerBeta.exe", check=True)

	if os.path.isfile("RobloxPlayerBeta.exe") and not os.path.isfile("RobloxPlayerBeta.exe.del"):
		subprocess.run("ren \"%cd%\\RobloxPlayerBeta.exe\" RobloxPlayerBeta.exe.del", check=True, shell=True)
		
	if os.path.isfile("RobloxPlayerLauncher.exe") and not os.path.isfile("RobloxPlayerLauncher.exe.del"):
		subprocess.run("ren \"%cd%\\RobloxPlayerLauncher.exe\" RobloxPlayerLauncher.exe.del", check=True, shell=True)

	subprocess.run("ren \"%cd%\\RobloxPlayerBeta_.exe\" RobloxPlayerBeta.exe", check=True, shell=True)
	subprocess.run("ren \"%cd%\\RobloxPlayerLauncher_.exe\" RobloxPlayerLauncher.exe", check=True, shell=True)
	
	subprocess.run("del RobloxPlayerBeta.exe.del", check=True, shell=True)
	subprocess.run("del RobloxPlayerLauncher.exe.del", check=True, shell=True)