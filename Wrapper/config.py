import os
import pickle
config = {
	"compressWrapper": True, # Compression for wrapper executables (it is recomended that you leave this on)
	"legacyMode": False # Use for older clients like the 2016 client (if they have an unexpected argument error then turn this on)
}

if os.path.isfile("config.dat"):
	configFile = open("config.dat", "rb")
	config = pickle.load(configFile)
	configFile.close()
def save():
	configFile = open("config.dat", "wb")
	pickle.dump(config, configFile)
	configFile.close()
def apply(obj):
	for k, v in config.items():
		obj[k] = v