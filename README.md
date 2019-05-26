NOTE: All important items for the Roblox-Wrapper are under the Wrapper folder. The Ahk2Exe source code is not required.
# Installation
## How to install:
  1. Clone this repository somewhere (it can be anywhere)
  2. Install python 3.5+ if you haven't
  3. Optionally manually extract to a specific version folder (it only works for RobloxPlayer as of now)
  4. Cd into the Wrapper folder or the Roblox version folder you manually extracted to
  5. Run `python install.py`
  6. Edit RobloxPlayerBeta.py or RobloxPlayerLauncher.py. These are what launch the real Roblox processes along with their arguments.
  5. You're done! Just hit play on a game and you're good to go!
## How to uninstall:
  1. Run `python uninstall.py` OR skip to step 2
  2. Optionally run `python cleanup.py` to clear all of the wrapper files. WARNING: this also clears both ahk scripts!
  3. RobloxPlayerBeta.py and RobloxPlayerLauncher.py files will be preserved.

# FAQ
## What is help.pyw?
Help.pyw opens the window for Roblox's argument list. These are player NOT launcher arguments.

## Can I install this on Mac?
No, you can't install this on Mac since it relies on AHK to compile the binaries to wrap Roblox.

## What can I use this for?
You can run commands when Roblox starts or set custom RobloxPlayer arguments. By default browser tracking id arguments are removed from launcher arguments and --fast is added to launcher arguments.

## What are the -a and -j arguments used for?
The -j (aka --joinScriptUrl) argument specifies the url that Roblox's servers use to set up your character.
The -a (aka --authenticationUrl) argument specifies the authentication url that Roblox's servers use to verify who you are.
You can't change these or you'll be kicked since they are verified on join.

## What is the -t argument?
The -t (aka --authenticationTicket) argument is how Roblox determines what account you're using. You used to be able to play as a guest by using an expired authentication ticket but this is no longer the case. Auth tickets will expire after roughly 30 seconds from my testing.
