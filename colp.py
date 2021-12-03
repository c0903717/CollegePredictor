from tkinter import *

import tkinter as tk
import tkinter.messagebox
root = tk.Tk()

frame1 = Frame(root)
root.title("College Acceptance Chance Predictor")

root.configure(bg='lightgreen')
frame2 = Frame(root)
root.title("tkinter frame")

root.geometry("1500x900")

length = 1200
width = 1000




'''label= Label(canvas,text="Label",justify=LEFT)
label.pack(side=LEFT)
'''
def say_hi():
    print("hello ~ !")
'''
tk.Label(canvas, text="Enter GPA Unweighted*").grid(row=0, column = 0)

tk.Label(canvas, text="Enter GPA Weighted*").grid(row=30, column = 0)

tk.Label(canvas, text="Enter Class Rank*").grid(row=60, column = 0)

tk.Label(canvas, text="Enter Sat Score(Optional but reccomended)").grid(row=90, column = 0)

tk.Label(canvas, text="Enter ACT Score(Optional but reccomended)").grid(row=120, column = 0)

tk.Label(canvas, text="Enter ACT Score(Optional but reccomended)").grid(row=150, column = 0)

tk.Label(canvas, text="Number of ECs related to major").grid(row=180, column = 0)

tk.Label(canvas, text="Number of ECs not related to major").grid(row=210, column = 0)

tk.Label(canvas, text="Choose Your Major").grid(row=0, column = 0)'''


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
   
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)

menubar.add_cascade(label="Help", menu=helpmenu)




def callbackgpau():
    strs = str(egpau.get())
    ints = float(strs)
    
    if strs.isnumeric == False or ints > 4 or ints < 2  :
        tkinter.messagebox.showerror('error','please enter a valid gpa')
      
    print (egpau.get()) # This is the text you may want to use later
def callbackgpaw():
    print (egpaw.get()) # This is the text you may want to use later
def callbackact():
    print (eact.get()) # This is the text you may want to use later
def callbacksat():
    print (esat.get()) # This is the text you may want to use later
def ecsr():
    print (ecs.get()) # This is the text you may want to use later
def ecsu():
    print (ecsu.get()) # This is the text you may want to use later

#user input boxes
labelent = Label( root,width = 50, text= "Welcome to College Predictor!")
labelent.place(x = 670, y = 800)


egpau = Entry(root)
egpau.place(x = 750, y = 70)

egpau.focus_set()

labelgpa = Label( root, text= "Enter GPA Unweighted*")
labelgpa.place(x = 590, y = 70)

bgpau = Button(root, text = "OK", width = 10, command = callbackgpau)
bgpau.place(x = 885, y = 70)



yval = 150

egpaw = Entry(root)
egpaw.place(x = 750, y = 110)

egpaw.focus_set()

labelgpaw = Label( root, text= "Enter GPA Weighted*")
labelgpaw.place(x = 590, y = 110)

bgpaw = Button(root, text = "OK", width = 10, command = callbackgpaw)
bgpaw.place(x = 885, y = 110)



eact = Entry(root)
eact.place(x = 750, y = 150)

eact.focus_set()

labelact = Label( root, text= "Enter ACT (Reccomended)")
labelact.place(x = 590, y = 150)

bact = Button(root, text = "OK", width = 10, command = callbackact)
bact.place(x = 885, y = 150)


esat = Entry(root)
esat.place(x = 750, y = 190)
esat.focus_set()
labelsat = Label( root, text= "Enter SAT (Reccomended)")
labelsat.place(x = 590, y = 190)
bsat = Button(root, text = "OK", width = 10, command = callbacksat)
bsat.place(x = 885, y = 190)

ecs = Entry(root)
ecs.place(x = 750, y = 230)
ecs.focus_set()
labelecs = Label( root, text= "# of ECs related to Major *")
labelecs.place(x = 590, y = 230)
bgecs = Button(root, text = "OK", width = 10, command = ecsr)
bgecs.place(x = 885, y = 230)

ecsu = Entry(root)
ecsu.place(x = 750, y = 270)
ecsu.focus_set()
labelecsu = Label( root, text= "# of ECs unrelated to Major *")
labelecsu.place(x = 590, y = 270)
bgecsu = Button(root, text = "OK", width = 10, command = ecsu)
bgecsu.place(x = 885, y = 270)


root.config(menu=menubar)

root.mainloop()
