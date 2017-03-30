# ############################################################## #
#                  - ABOUT THE PROGRAM -
# Program name : tkinter line drawer
# Program description : draws line on button click
# Author : Abdur-Rahmaan Janhangeer
# Date : 30th of March 2017
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
# 4 Canva and frame
# 5 mainloop
# ############################################################# #
# ############################################################# #
#                   - CONVENTIONS USED -
# --- naming ---
# functions : function names end with F save line()
# initials naming used. Label -> l ,l2 etc
# ############################################################# #
# ############################################################# #
#                  - NOTES AND WARNINGS -
# ---warning---
# wildcard operator used in imports
# no input validation. check add-num.py for demo. here canva 
#     focused on
# ---notes---
# one shot comments used
# ############################################################# #
from tkinter import *

root = Tk() #you can name it fruit, banana, master etc instead of root
root.title("line drawer")

def line(x,y,x2,y2,col,w): #just to make syntax nicer
    c.create_line(x,y,x2,y2,fill =col,width =w)

def drawLine():
    x =float(e.get()) #returns string so cating required
    y =float(e2.get())
    x2 =float(e3.get())
    y2 =float(e4.get())
    w =float(e5.get())
    col =e6.get() #no cating required. colour can also be in hex 
    line(x,y,x2,y2,col,w)

c =Canvas(root, height=250, width =300, bg ="white")
c.grid(row =0, column =0)
line(10,10,100,100,"black",2) #one line already drawn when app loads

f =Frame(root) #frame enables component grouping
f.grid(row =0, column =1, sticky="n")

l =Label(f, text="x1")
l.grid(row =0, column =0)
e =Entry(f)
e.grid(row =1, column =0)

l2 =Label(f, text="y1")
l2.grid(row =2, column =0)
e2 =Entry(f)
e2.grid(row =3, column =0)

l3 =Label(f, text="x2")
l3.grid(row =4, column =0)
e3 =Entry(f)
e3.grid(row =5, column =0)

l4 =Label(f, text="y2")
l4.grid(row =6, column =0)
e4 =Entry(f)
e4.grid(row =7, column =0)

l5 =Label(f, text="width")
l5.grid(row =8, column =0)
e5 =Entry(f)
e5.grid(row =9, column =0)

l6 =Label(f, text="colour")
l6.grid(row =10, column =0)
e6 =Entry(f)
e6.grid(row =11, column =0)

b =Button(f, text ="draw line", command =drawLine) #here command binded to click on button
b.grid(row =12, column =0)

root.mainloop()
