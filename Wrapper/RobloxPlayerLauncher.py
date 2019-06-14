# A python file which launches Roblox! Specify your own code if you'd like and then run install.py!

import subprocess
from subprocess import STDOUT, PIPE
import os
import sys

sys.argv[0] = "RobloxPlayerLauncher_.exe"

print(sys.argv)
try:
	subprocess.run(args=sys.argv, stdout=PIPE, stderr=STDOUT)
except:
	subprocess.run("pause")