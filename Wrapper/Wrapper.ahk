#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

name := SubStr(A_ScriptName, 1, -4)
args := ""

for key, val in a_args
	args := args " " val

logFile := FileOpen("./" name ".log", "w")
logFile.Write(args)

Run, % "python " name ".py" args