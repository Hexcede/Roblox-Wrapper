# A python file which launches Roblox Studio! Specify your own code if you'd like and then run install.py!

import subprocess
from subprocess import STDOUT, PIPE
import os
import sys

sys.argv[0] = sys.argv[0][:-3]+".exe" # Use the script's name to find the target program

print(sys.argv)
try:
	import installUtil
	installUtil.runner(sys.argv)
except:
	subprocess.run("pause")