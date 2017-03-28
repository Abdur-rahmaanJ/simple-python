# ############################################################## #
#                  - ABOUT THE PROGRAM -
# Program name : tkinter radio button background changer
# Program description : changes program background on radio button
#                       click
# Author : Abdur-Rahmaan Janhangeer
# Date : 26th of March 2017
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
# 4 Widgte variable definition ans state set
# 5 radio button
# 6 mainloop
# ############################################################# #
# ############################################################# #
#                   - CONVENTIONS USED -
# --- naming ---
# functions : function names end with F
# radio buttons named choice1 . . .
# ############################################################# #
# ############################################################# #
#                  - NOTES AND WARNINGS -
# ---warning---
# wildcard operator used in imports
# ---notes---
# one shot comments used
# ############################################################# #

from tkinter import *

root = Tk() #you can name it fruit, banana, master etc instead of root
root.title("radio button background changer")

def changeColourF(colour): # eliminates need for different functions
    root.configure(background =colour)
    choice1.configure(background =colour) # if not, a dirty grey patch appears below radio button text
    choice2.configure(background =colour)
    choice3.configure(background =colour)
    choice4.configure(background =colour)
    
v =StringVar()
v.set("L") # state on begining

choice1 =Radiobutton(root, text ="red", value =1, variable =v, command =lambda: changeColourF("red")) 
choice1.grid(row =0, column =0) #lambda for parameter passing

choice2 =Radiobutton(root, text ="blue", value =2, variable =v, command =lambda: changeColourF("blue"))
choice2.grid(row =1, column =0)

choice3 =Radiobutton(root, text ="yellow", value =3, variable =v, command =lambda: changeColourF("yellow"))
choice3.grid(row =2, column =0)

choice4 =Radiobutton(root, text ="green", value =4,  variable =v, command =lambda: changeColourF("green"))
choice4.grid(row =3, column =0)

root.mainloop()
