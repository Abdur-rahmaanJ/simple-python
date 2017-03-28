# ############################################################## #
# - ABOUT THE PROGRAM -
# Program name : tkinter addition calculator
# Program description : takes two digit as input and calculates
# the sum of it. Provides good validation
# feedbacks
# Author : Abdur-Rahmaan Janhangeer
# Date : 22nd of March 2017
# License : MIT with emphasis :
# You are free to modify and distribute the program provided that
# attribution is C L E A R L Y made.
# Python version : Python 3.4
# ############################################################# #
# ############################################################# #
# - INDEX -
# 1 import statement/s
# 2 root / master definition
# 3 Labels and Entry
# 4 calculation function and input validation
# 5 status label
# 6 mainloop
# ############################################################# #
# ############################################################# #
# - CONVENTIONS USED -
# --- naming ---
# variables : snake_case
# functions : function names end with F
# number : abbreviated to num like num1
# textbox / entry : abbreviated to txtbx
# ############################################################# #
# ############################################################# #
# - NOTES AND WARNINGS -
# ---warning---
# wildcard operator used in imports
# ---notes---
# see explanations at the end
# ############################################################# #

from tkinter import *

root = Tk()
root.title("Addition Calculator")

answer_label =Label(root, text ="---")
answer_label.grid(row =0, column =0)

label1 =Label(root, text ="first")
label1.grid(row =1, column =0)

num1_txtbx =Entry(root)
num1_txtbx.grid(row =1, column =1)

label2 =Label(root, text ="second")
label2.grid(row =2, column =0)

num2_txtbx =Entry(root)
num2_txtbx.grid(row =2, column =1)

def addF():
    if (num1_txtbx.get() and num2_txtbx.get() != ""):
        try:
            num1 =float(num1_txtbx.get())
            num2 =float(num2_txtbx.get())

            answer= num1 + num2
            answer_label.configure(text =answer)
            status_label.configure(text ="successfully computed")
        except:
            status_label.configure(text ="invalid input, check your input types")
    else:
        status_label.configure(text ="fill in all the required fields")

calculate_button =Button(root, text="calculate", command= addF)
calculate_button.grid(row =3, column =0, columnspan =2)

status_label =Label(root, height =5, width =25, bg ="black", fg ="#00FF00", text ="---", wraplength =150)
status_label.grid(row =4, column =0, columnspan =2)

root.mainloop()

# ############################################################# #
# POINTS OF NOTE #
# ################
# -in the addF function, the input is checked for emptiness and
# type error
# -in the status_label , the text colour has been specified using
# the hex format
# -wraplength is used to specify the width after which the text
# goes on a new line
# ############################################################# #
