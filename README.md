## What is this?
Roblox Wrapper is a tool which wraps Roblox installations and prevents them from being removed.
It also allows you to see the arguments Roblox is ran with and even modify them!
Every wrapped Roblox executable will run a single python script which launches the real Roblox executables.

Roblox Wrapper also includes support for old Roblox versions such as the 2016 player!
Sadly it's not possible to join a real Roblox game using the 2016 client for various (probably obvious) reasons.

## How to install:
  1. Install python 3.5+ if you haven't
  2. Optionally extract the wrapper to a specific version folder
  3. Double click `command-window.cmd`
  4. Run `python install.py` to install for Roblox Player (see command line arguments below for studio installs)
  5. You're done! Just hit play on a game and you should see a command window pop up with all of the arguments Roblox was run with.
## How to uninstall:
  1. Run `python uninstall.py`
  2. Optionally add `-c` or `--cleanup` to completely uninstall (the installed Roblox version will look exactly the same as it did before installation)

## Command line arguments
### install.py
`--studio` (`-s`) - Will install for studio.
`--legacy` (`-l`) - Will install and enable legacyMode in the config. Can be used to run old clients like the 2016 client. Without this, old clients will show an error messaging saying something like `unrecognized launch option '--launchtime=1560551643876'`.
### uninstall.py
`--studio` (`-s`) - Will uninstall for studio.
`--cleanup` (`-c`) - Will cleanup *all* wrapper files.

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
