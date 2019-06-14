# A python file which launches Roblox Player! Specify your own code if you'd like and then run install.py!

import subprocess
from subprocess import STDOUT, PIPE
import os
import sys
import re

sys.argv[0] = "RobloxPlayerBeta_.exe"
sys.argv.insert(1, "--fast")

try:
	browserTrackingIndex = sys.argv.index("-b")
	sys.argv.pop(browserTrackingIndex)
	sys.argv.pop(browserTrackingIndex)
	print("Successfully removed tracking id")
except:
	None

try:
	joinIndex = sys.argv.index("-j")+1
	sys.argv[joinIndex] = re.sub(r"&browserTrackerId=\d+", "", sys.argv[joinIndex])
	print("Sucessfully removed tracking id from join script")
except:
	None

print(sys.argv)
try:
	subprocess.run(args=sys.argv, stdout=PIPE, stderr=STDOUT)
except:
	subprocess.run("pause")