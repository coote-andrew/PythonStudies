#!/usr/bin/python

from tkinter import *
from tkinter import ttk
import sys
import time


   # Timer
import time


# Variables to keep track and display



def startPause():
    global breakTimeSec
    global breakTimeMin
    global workTimeSec
    global workTimeMin
    global breakTimeSecDef
    global breakTimeMinDef
    global workTimeSecDef
    global workTimeMinDef
    print("This is the timer")
   
    totalTrue = True
    # Begin Process
    while totalTrue:
        
        breakTimeLoop = True
        while breakTimeLoop:
            print('break ', end='')
            if breakTimeSec == 0:
                breakTimeSec = 60
                breakTimeMin = breakTimeMin.get() - 1
            breakTimeSec = breakTimeSec.get() - 1
            print(str(breakTimeMin) + " Mins " + str(breakTimeSec) + " Sec ")
            time.sleep(1)
            if breakTimeSec == 0 and breakTimeMin ==0:
                breakTimeSec = breakTimeSecDef
                breakTimeMin = breakTimeMinDef
                breakTimeLoop = False
                workTimeLoop = True
                
            if breakTimeSec == 0:
                breakTimeSec = 60
                breakTimeMin = breakTimeMin.get() - 1

           

        while workTimeLoop:
            print('work ', end='')
            if workTimeSec == 0:
                workTimeSec = 60
                workTimeMin -= 1
            workTimeSec -= 1
            print(str(workTimeMin) + " Mins " + str(workTimeSec) + " Sec ")
            time.sleep(1)

            if workTimeSec == 0 and workTimeMin ==0:
                workTimeSec = workTimeSecDef
                workTimeMin = workTimeMinDef
                workTimeLoop = False
                breakTimeLoop = True
                
            if workTimeSec == 0:
                workTimeSec = 60
                workTimeMin -= 1




root = Tk()
root.title('pomodoro timer')
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)
breakTimeSec = IntVar()
breakTimeMin = IntVar()
workTimeSec = IntVar()
workTimeMin = IntVar()
breakTimeSecDef = IntVar()
breakTimeMinDef = IntVar()
workTimeSecDef = IntVar()
workTimeMinDef = IntVar()
breakTimeSec.set(10)
breakTimeMin.set(10)
workTimeSec.set(10)
workTimeMin.set(10)
breakTimeSecDef.set(10)
breakTimeMinDef.set(10)
workTimeSecDef.set(10)
workTimeMinDef.set(10)
breakTimeSecDef_entry = ttk.Entry(mainframe, width=7, textvariable=breakTimeSecDef)
breakTimeSecDef_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, textvariable=breakTimeSec).grid(column=2, row=2, sticky=(W,E))
ttk.Button(mainframe, text="Start/Pause", command=startPause).grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, textvariable=breakTimeMin).grid(column=3, row=1, sticky=(W,E))
for child in mainframe.winfo_children():child.grid_configure(padx=5, pady=5)
breakTimeSecDef_entry.focus()

