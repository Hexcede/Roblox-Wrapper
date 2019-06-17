## What is this?
Roblox Wrapper is a tool which wraps Roblox installations and prevents them from being removed.
It also allows you to see the arguments Roblox is ran with and even modify them!
Every wrapped Roblox executable will run a single python script which launches the real Roblox executables.

Roblox Wrapper also includes support for old Roblox versions such as the 2016 player!
Sadly it's not possible to join a real Roblox game using the 2016 client for various (probably obvious) reasons.

## How to install:
  1. Install python 3.5+ if you haven't
  2. Optionally extract the wrapper to a specific version folder
  3. Double click `command-window.cmd` to open a command window in the wrapper directory.
  4. Run `python install.py` to install for Roblox Player (see command line arguments below for studio installs)
  5. You're done! Just hit play on a game and you should see a command window pop up with all of the arguments Roblox was run with.
## How to uninstall:
  1. Run `python uninstall.py`
  2. Optionally add `-c` or `--cleanup` to completely uninstall (the installed Roblox version will look exactly the same as it did before installation)

## Command line arguments
### install.py
`--studio` (`-s`) - Will install for the latest studio version.
`--legacy` (`-l`) - Will install and enable legacyMode in the config file. Can be used to run old clients like the 2016 client. Without this, old clients will show an error messaging saying something like `unrecognized launch option '--launchtime=1560551643876'`. NOTE: This does not affect studio installs.
### uninstall.py
`--studio` (`-s`) - Will uninstall for the latest studio version.
`--cleanup` (`-c`) - Will do a full uninstall of the wrapper. A normal uninstall will not remove any wrapper files and instead will just unlink the wrapper.

# FAQ
## What is help.pyw?
Help.pyw opens the window for Roblox's argument list.

## Can I install this on Mac?
No, you can't install this on Mac since it relies on AHK to compile the wrapper binaries.

## What can I use this for?
You can install custom Roblox versions, or set custom arguments. By default the browser tracking id is removed from the launcher arguments/join script.

## What are the -j and -a arguments used for?
The -j (aka --joinScriptUrl) argument specifies the url that Roblox uses to locate the server you want to join.
The -a (aka --authenticationUrl) argument specifies the authentication url that Roblox's servers use to log you into the game.
You can't change these from their default locations or you'll be disconnected, however, you can change the query arguments. (e.g. placeId)

## What is the -t argument?
The -t (aka --authenticationTicket) argument is how Roblox determines what account you're using. When Roblox connects to a server it will use this temporary ticket to log you in.

# Installing an old Roblox version
  1. Locate the latest version folder (Will be located in %localappdata%\Roblox\Versions)
  2. Open the folder
  3. Delete everything inside of the folder (back it up if you want to)
  4. Copy the contents of the Roblox version you want to install into the folder
  5. Run the wrapper installer (you may want to use the -l option if you're using an older version of Roblox Player, studio installs will be unaffected)
