# ############################################################## #
#                  - ABOUT THE PROGRAM -
# Program name : open new window app
# Program description : opens new window on button click
# Author : Abdur-Rahmaan Janhangeer
# Date : 7th of May 2017
# License : MIT with emphasis :
# You are free to modify and distribute the program provided that
# attribution is  C L E A R L Y  made.
# Python version : Python 3.4
# ############################################################# #
# ############################################################# #
#                      - INDEX -
# 1 import statement/s
# 2 root / master definition
# 3 Function definition
# 4 Button 
# 5 mainloop
# ############################################################# #
# ############################################################# #
#                   - CONVENTIONS USED -
# --- naming ---
# functions : function names end with F
# Button named button1 . . .
# ############################################################# #
# ############################################################# #
#                  - NOTES AND WARNINGS -
# ---warning---
# wildcard operator used in imports
# ---notes---
# one shot comments used
# ############################################################# #

from tkinter import *

root = Tk()

def new_winF(): # new window definition
    newwin = Toplevel(root)
    display = Label(newwin, text="Humm, see a new window !")
    display.pack()    

button1 =Button(root, text ="open new window", command =new_winF) #command linked
button1.pack()

root.mainloop()
