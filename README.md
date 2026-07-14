# Searchy
 A lightning fast searching tool written in bash for linux, with a CLI & GUI interface. This program can take long to search if you have another big partition/drive mounted, but it isn't as slow as before. This *is* case-insensitive.

 # Dependencies for CLI version
 * Unix-like operating system
 * Bash/zsh shell (as far as I have tested)
 # Dependencies for GUI version
 * Unix-like operating system
 * Bash/zsh shell (as far as I have tested)
 * Python 3, tkinter
 # A bit more info 
 **This tool first asks what you want to search for, then searches the entire `/` directory for the file you're looking for (or the one you selected), without having to use `sudo`! It ignores all error messages, but does inform you if the file you're looking for can't be found. It prunes out useless system directories such as `/proc` and `/tmp` to speed up searching drastically! This is case-insensitive, for example if you type 8VerT.Py, but the file is actually called 8vert.py, it will still find it, but if you make a *typo*, then the program won't be able to find it. I will look into fixing this, though.**
 # Contact
 **CONTACT ME AT `kmoruihrdp@hotmail.com`, OR IN THE GITHUB DISCUSSIONS PAGE OF THIS REPO, FOR FEEDBACK, TROUBLESHOOTING, QUERIES AND SUGGESTIONS!!**
