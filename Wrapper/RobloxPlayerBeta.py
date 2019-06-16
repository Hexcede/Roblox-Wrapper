# A python file which launches Roblox Player! Specify your own code if you'd like and then run install.py!

import subprocess
from subprocess import STDOUT, PIPE
import os
import sys
import re

from config import apply
apply(globals())

sys.argv[0] = sys.argv[0][:-3]+".exe" # Use the script's name to find the target program

# Argument manipulation:
sys.argv.insert(1, "--fast") # Add the --fast argument
try:
	browserTrackingIndex = sys.argv.index("-b") # Get tracking id location
	sys.argv.pop(browserTrackingIndex) # Remove -b
	sys.argv.pop(browserTrackingIndex) # Remove the value
	print("Successfully removed tracking id")
except:
	None
try:
	joinIndex = sys.argv.index("-j")+1 # Get join script location
	sys.argv[joinIndex] = re.sub(r"&browserTrackerId=\d+", "", sys.argv[joinIndex]) # Parse out tracking id from join script url
	print("Sucessfully removed tracking id from join script")
except:
	None

if legacyMode:
	for index, value in enumerate(sys.argv):
		if value.startswith("--launchtime"): # For some reason the format is different than any other variable (--launchtime=value)
			sys.argv.pop(index)
			print("Successfully removed --launchtime (legacyMode)")
	
	try:
		rloc = sys.argv.index("--rloc")
		sys.argv.pop(rloc) # Remove --rloc
		sys.argv.pop(rloc) # Remove the value
		print("Successfully removed --rloc (legacyMode)")
	except:
		None
	try:
		gloc = sys.argv.index("--gloc")
		sys.argv.pop(gloc) # Remove --gloc
		sys.argv.pop(gloc) # Remove the value
		print("Successfully removed --gloc (legacyMode)")
	except:
		None

print(sys.argv)
try:
	import installUtil
	installUtil.runner(sys.argv)
except:
	subprocess.run("pause")